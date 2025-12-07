#!/usr/bin/python3
"""This is docstr
"""
import requests
request = requests.get("https://intranet.hbtn.io/status")
response = request.text
print("Body response:")
print("\t- type: {}".format(type(response)))
print("\t- content: {}".format(response))
