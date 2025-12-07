#!/usr/bin/python3
"""This script"""
import urllib.request
import sys
if __name__ == "__main__":
    """this is cp,,emt"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        read = r.getheader("X-Request-Id")
        print(read)
