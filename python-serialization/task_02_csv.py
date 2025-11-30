#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # CSV faylını oxuyuruq
        with open(csv_filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        # JSON formatına serialize edib data.json-a yazırıq
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
