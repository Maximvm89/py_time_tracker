import json
import os
import time

import psutil
import win32gui
import win32process

# Folder where to store time tracking data
document_path = os.path.join(os.environ["USERPROFILE"], "Documents", "time_track")
if not os.path.isdir(document_path):
    os.makedirs(document_path)


class TimeTracker:
    def __init__(self):
        self.windows = {}
        self.i = 0
        self.document_path = os.path.join(os.environ["USERPROFILE"], "Documents", "time_track")
        self.data_out_json = ""

    def __print_seconds(self, seconds):
        minutes, secs = divmod(seconds, 60)
        hour, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hour, minutes, secs)

    def start_tracking(self, task_name="Default"):
        # let's check if a json file already exists
        self.data_out_json = os.path.join(document_path, task_name + '.json')
        print "[+] Looking for {}".format(self.data_out_json)
        if os.path.isfile(self.data_out_json):
            # If the file exists we want to load the dictionary data instead of starting from scratch
            try:
                with open(self.data_out_json) as f:
                    self.windows = json.load(f)
            except ValueError:
                print "[-] Problem reading {}. Storing json into {}_temp".format(self.data_out_json, task_name)
                self.data_out_json = os.path.join(document_path, task_name + '_temp.json')

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

    def stop_tracking(self):
        print "Received keyboard interrupt"
        self.i = 2  # should interrupt the tracking
        with open(self.data_out_json, "w") as out_file:
            json.dump(self.windows, out_file, indent=1)


def stop_tracking():
    pass


if __name__ == '__main__':
    t_tracker = TimeTracker()
    try:
        t_tracker.start_tracking("building_time_tracker")
    except KeyboardInterrupt:
        t_tracker.stop_tracking()
