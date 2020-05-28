'''
Name: time_tracker.py
Author: Marco Parisi
Date: 28/05/2020
Version: 0.0
DESCRIPTION
---------------
Simple time tracker script to track your time
'''

import argparse
import datetime
import json
import os
import time

import psutil
import win32gui
import win32process


class TimeTracker:
    def __init__(self):
        self.windows = {}
        self.i = 0
        today_date = datetime.datetime.today().strftime("%a_%d_%b_%Y")
        self.document_path = os.path.join(os.environ["USERPROFILE"], "Documents", "time_track",
                                          today_date)
        if not os.path.isdir(self.document_path):
            print "[+] Creating folder {}".format(self.document_path)
            os.makedirs(self.document_path)
        self.data_out_json = ""

    def __print_seconds(self, seconds):
        minutes, secs = divmod(seconds, 60)
        hour, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hour, minutes, secs)

    def start_tracking(self, task_name="Default"):
        # let's check if a json file already exists
        self.data_out_json = os.path.join(self.document_path, task_name + '.json')
        if os.path.isfile(self.data_out_json):
            print "[+] Found an existing {}".format(self.data_out_json)
            print "[+] Loading previous time track data"
            # If the file exists we want to load the dictionary data instead of starting from scratch
            try:
                with open(self.data_out_json) as f:
                    self.windows = json.load(f)
            except ValueError:
                print "[-] Problem reading {}. Storing json into {}_temp".format(self.data_out_json, task_name)
                self.data_out_json = os.path.join(self.document_path, task_name + '_temp.json')
        else:
            print "[+] Creating a new time track data instance"

        while self.i <= 1:
            time.sleep(3)
            w = win32gui
            w.GetWindowText(w.GetForegroundWindow())
            pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
            try:
                process_name = psutil.Process(pid[-1]).name()
            except psutil.NoSuchProcess as e:
                process_name = "Unknown process:{}".format(pid[-1])
            try:
                time_spent = self.windows[process_name] + 3
            except KeyError as e:
                # no value in the dictionary
                time_spent = 0
            self.windows[process_name] = time_spent
            total_time_seconds = 0
            print "[+] For task {}".format(task_name)
            for key, value in self.windows.items():
                print "[+]\t\t {} : {}".format(key, self.__print_seconds(value))
                total_time_seconds += value

            print "[+] Total time spent :{}".format(self.__print_seconds(total_time_seconds))
            # every minute let's dump data, just to avoid to lose info
            if total_time_seconds % 60 == 0:
                self.__dump_data()

    def __dump_data(self):

        print "[+] Saving data in {}".format(self.data_out_json)
        with open(self.data_out_json, "w") as out_file:
            json.dump(self.windows, out_file, indent=1)

    def stop_tracking(self):
        print "[-] Received keyboard interrupt"
        print "[-] Time tracker interrupted"
        self.i = 2  # should interrupt the tracking
        self.__dump_data()
        y = "y"
        n = "n"
        # Show the task available
        # Create a new task
        print "[+] Do you want to start track a new task? [y][n]"
        user_input = input()
        if user_input.lower() == "y":
            print "[+] Insert the name of the new task to track:"
            user_input = raw_input()
            self.i = 0
            self.windows = {}
            try:
                self.start_tracking(user_input)
            except KeyboardInterrupt:
                self.stop_tracking()

        else:
            print "[+] Do you want to continue an existing task? [y][n]"
            user_input = input()
            if user_input.lower() == "y":
                print "[-] Task available"
                # Create a dictionary of possible task to switch in
                available_tasks = {}
                for dirpath, dirnames, filenames in os.walk(self.document_path):
                    count = 0
                    for json_file in filenames:
                        if json_file.endswith(".json"):
                            print "\t[{}] {}".format(count, json_file.replace(".json", ""))
                            available_tasks[count] = json_file.replace(".json", "")
                            count += 1
                print "[-] Select the number of the task you want to switch back"
                user_input = raw_input()
                try:
                    self.i = 0
                    self.windows = {}
                    try:
                        self.start_tracking(available_tasks[int(user_input)])
                    except KeyboardInterrupt:
                        self.stop_tracking()
                except KeyError:
                    print "[-] Error: couldnt find any task with the input:{}".format(user_input)
            else:
                print "[+] Closing time tracker"
                exit()


def stop_tracking():
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Time tracker built by Marco Parisi")
    parser.add_argument('task_name', type=str)

    args = parser.parse_args()

    t_tracker = TimeTracker()
    try:
        t_tracker.start_tracking(args.task_name)
    except KeyboardInterrupt:
        t_tracker.stop_tracking()
