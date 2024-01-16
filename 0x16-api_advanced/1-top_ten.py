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
    headers = {'User-Agent': 'alx-lisa-api'}

    # Construct API URL for hot posts
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # Make request
    response = requests.get(url, headers=headers)

    # Check if response is successful/invalid
    if response.status_code == 200:
        posts_data = response.json().get('data', {}).get('children', [])

        # Check if subreddit exists
        for post in post_data:
            print(post['data']['title'])
    elif response.status_code == 404:
        print('None')
    else:
        print('None')
