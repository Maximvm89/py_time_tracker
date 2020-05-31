"""
Name: format_data.py
Author: Marco Parisi
Date: 31/05/2020
Version: 0.0
DESCRIPTION
---------------
Reads the json files produces by the time tracker and build a csv with the result of the data

"""

import argparse
import csv
import datetime
import json
import os


def build_report(path_to_tracks, format_time=False):
    tracking_data = {}
    document_path = path_to_tracks

    csv_file = os.path.join(document_path, "total.csv")
    for dirpath, dirnames, filenames in os.walk(document_path):
        for json_file in filenames:
            if json_file.endswith(".json"):
                with open(os.path.join(dirpath, json_file)) as f:
                    task = json.load(f)
                    tracking_data[json_file.replace(".json", "")] = task

    def __print_seconds(seconds):
        minutes, secs = divmod(seconds, 60)
        hour, minutes = divmod(minutes, 60)
        return "%d.%02d.%02d" % (hour, minutes, secs)

    windows_header = [u"task_name"]
    # pprint.pprint(tracking_data)
    for key, value in tracking_data.items():
        for key2, value2 in value.items():
            if key2 not in windows_header:
                windows_header.append(key2)

    # pprint.pprint(tracking_data)
    # pprint.pprint(windows_header)
    with open(csv_file, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=windows_header)
        writer.writeheader()
        for key, value in tracking_data.items():
            # formatted_comma_string = "{},".format(key)  # Name of the task
            formatted_comma_string = ""
            for window in windows_header:
                try:
                    if window == "task_name":
                        formatted_comma_string += "{},".format(key)
                    elif value[window]:
                        if format_time:
                            formatted_comma_string += "{},".format(__print_seconds(value[window]))
                        else:
                            formatted_comma_string += "{},".format(value[window])
                except KeyError:
                    if format_time:
                        formatted_comma_string += "00.00.00,"
                    else:
                        formatted_comma_string += "0,"

            formatted_comma_string += "\n"
            csv_file.write(formatted_comma_string)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Build the report")
    parser.add_argument('path_to_folder', type=str)
    parser.add_argument('-fs, --format_seconds', type=bool,
                        help="If this flag is specified it will print data with nice formatting")

    args = parser.parse_args()

    if not os.path.isdir(args.path_to_folder):
        print("This is not a folder path {}".format(args.path_to_folder))
        print("Please provide a correct path folder")

    else:
        build_report(args.path_to_folder)
