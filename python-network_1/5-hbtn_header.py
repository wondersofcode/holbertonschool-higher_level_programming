#!/usr/bin/python3
"""this is docstr
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers["X-Request-Id"])
