#!/usr/bin/python3
"""Task 0"""


import json


def serialize_and_save_to_file(data, filename):
    """Task 0 """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Task 0 """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
