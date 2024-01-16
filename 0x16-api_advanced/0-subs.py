#!/usr/bin/python3

"""
A module that contains a function "number_of_subscribers".
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
    subreddit: The name of the subreddit.

    Returns:
    int: The number of subscribers. If the subreddit is invalid,
    return 0.
    """

    # Set custom User-Agent
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/jane_doe)'}

    # Construct API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Make request
    response = requests.get(url, headers=headers)

    # Check if  response is successful/invalid
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0