#!/usr/bin/python3
"""Read and print a UTF-8 text file"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
