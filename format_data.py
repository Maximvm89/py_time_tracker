import csv
import json
import os
import datetime
import pprint

tracking_data = {}
today_date = datetime.datetime.today().strftime("%a_%d_%b_%Y")
document_path = os.path.join(os.environ["USERPROFILE"], "Documents", "time_track",
                                  today_date)
for dirpath, dirnames, filenames in os.walk(document_path):
    for json_file in filenames:
        if json_file.endswith(".json"):
            with open(os.path.join(dirpath, json_file)) as f:
                task = json.load(f)
                tracking_data[json_file.replace(".json", "")] = task

pprint.pprint(tracking_data)