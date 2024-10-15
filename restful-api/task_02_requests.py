#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Statue code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        with open("posts.csv", "w", newline='') as file:
            file.write(str(data))
