#!/usr/bin/python3
"""this is code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print("Email: {}".format(email))
