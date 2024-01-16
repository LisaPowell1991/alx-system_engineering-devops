#!/usr/bin/python3

"""
A module with a function "recurse
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively fetches the titles of all hot articles
    for a given subreddit using the Reddit API.

    Parameters:
    - subreddit (str): The name of subreddit.
    - hot_list (list): A list to store the titles of hot articles.

    Returns:
    List of titles of hot articles in the given subreddit.
    None: If subreddit is invalid or if no results are found.
    """
    if not hot_list:
        hot_list = {}

        # Set custom User-Agent
        headers = {
                  'User-Agent': 'alx-lisa-api:v1.0.0 (by /u/CaptainDiligent877'
                  }

        # Construct API URL
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

        # Make request
        response = requests.get(url, headers=headers)

        # Check if response is successful/invalid
        if response.status_code == 200:
            data = response.json()

            if 'data' in data and 'children' in data['data']:
                titles = [child['data']['title']
                          for child in data['data']['children']]
                hot_list.extend(titles)

                # Check if there are more pages (pagination)
                if 'after' in data['data']:
                    return recurse(subreddit, hot_list=hot_list)
                else:
                    return hot_list
            else:
                return hot_list if hot_list else None
        else:
            return None
