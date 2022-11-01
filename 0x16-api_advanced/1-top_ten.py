#!/usr/bin/python3
"""Script that prints out top ten hottest gists
of a subreddit"""
import requests


def top_ten(subreddit):
    """Function that fetches top 10 gists"""
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    try:
        response = requests.get(
            apiUrl, headers={"user-agent": userAgent}, allow_redirects=False)
        list_obj = response.json()['data']['children']

        for num in range(0, 10):
            print(list_obj[num]['data']['title'])

    except Exception:
        print('None')
