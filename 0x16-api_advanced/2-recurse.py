#!/usr/bin/python3
"""fetch data from the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after= ""):
    """gets a list containing the title of all hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    header = {'User-Agent': "Efe"}
    data = requests.get("{}".format(url, 10), headers=header).json()
    if data.get('error'):
        return None

    posts = data.get('data').get('children')
    titles = [post['data']['title'] for post in posts]
    hot_list = hot_list + titles
    after = data.get('data').get('after')
    if not after:
        return hot_list[:]
    return recurse(subreddit, hot_list, after)
