#!/usr/bin/python3
"""fetch data from the Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': "Efe"}
    data = requests.get("{}?limit={}".format(url, 10), headers=header).json()
    if data.get('data'):
        posts = data.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
