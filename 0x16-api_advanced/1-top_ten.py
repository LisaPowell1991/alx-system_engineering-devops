#!/usr/bin/python3


"""
A module that contains a function top_ten.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the
    titles of the first 10 hot posts
    for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    Prints the titles  of the first 10 hot posts
    Or None if the subreddit is invalid
    """
    # Set custom User-Agent
    headers = {'User-Agent':
               'linux:0x16.api.advanced:v1.0.0 (by /u/CaptainDiligent877)'}

    # Construct API URL for hot posts
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {"limit": 10}

    # Make request
    response = requests.get(url, headers=headers, params=params)

    # Check if response is successful/invalid
    if response.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
