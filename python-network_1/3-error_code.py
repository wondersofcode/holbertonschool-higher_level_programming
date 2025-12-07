#!/usr/bin/python3
"""this is docstr"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            r = response.read().decode("utf-8")
            print(r)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
