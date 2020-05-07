#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    request = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit),
                           params={"after": after},
                           headers={"User-Agent": "User-Agent"})
    return recurse(subreddit, hot_list, after)
    return hot_list
