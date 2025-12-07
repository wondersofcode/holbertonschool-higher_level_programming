#!/usr/bin/python3
"""this is script
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        r = response.json()
        print(r.get("id"))
    else:
        print(None)
