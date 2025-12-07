#!/usr/bin/python3
"""REQUESTs"""


import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    for i in response.json():
        print(i["title"])

def fetch_and_save_posts():
    response = requests.get(url)
    posts = response.json()

    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        for post in posts:
            writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})
