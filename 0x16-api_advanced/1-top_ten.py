#!/usr/bin/python3
"""contains 1 function: top_ten"""

import requests


def top_ten(subreddit):
    user = {"User-Agent": "custom"}
    request = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers=user)
    try:
        for i in range(10):
            print(request.json()
                  .get("data").get("children")[i].get("data").get("title"))
    except:
        print("None")
