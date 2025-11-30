#!/usr/bin/python3
"""Task 6"""


import json


def load_from_json_file(filename):
    """Task 6"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
