#!/usr/bin/python3
"""fetch data from the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': "Efe"}
    data = requests.get(url, headers=header).json()
    if data.get('error'):
        subscribers = 0
    else:
        subscribers = data.get('data').get('subscribers')
    return subscribers
