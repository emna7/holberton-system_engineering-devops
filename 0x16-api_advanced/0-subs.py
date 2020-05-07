#!/usr/bin/python3
"""returns the number of subs to a subreddit"""

import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "custom"}

    request = requests.get("https://www.reddit.com/r/{}/about.json"
                 .format(subreddit), headers=user)
    try:
        return request.json().get("data").get("subscribers")
    except:
        return(0)
