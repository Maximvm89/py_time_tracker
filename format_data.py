import csv
import datetime
import json
import os
import pprint

tracking_data = {}
today_date = datetime.datetime.today().strftime("%a_%d_%b_%Y")
document_path = os.path.join(os.environ["USERPROFILE"], "Documents", "time_track",
                             today_date)

document_path = r"C:\Users\marco\Documents\time_track\Thu_28_May_2020"
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
        formatted_comma_string = "{},".format(key)  # Name of the task
        print key
        print value
        for window in windows_header:
            print window
            try:
                if value[window]:
                    print value[window]
                    formatted_comma_string += "{},".format(__print_seconds(value[window]))
            except KeyError:
                formatted_comma_string += ","

        formatted_comma_string += "\n"
        csv_file.write(formatted_comma_string)