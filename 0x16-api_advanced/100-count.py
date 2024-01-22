#!/usr/bin/python3
"""
A module containing a function "count_words".
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    :param subreddit: The subreddit to query.
    :param word_list: List of keywords to count.
    :param after: Reddit API parameter for pagination.
    :param counts: Dictionary to store count of each keyword.
    """
    if counts is None:
        counts = {}

    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {"limit": 100, 'after': after}
    headers = {'User-Agent': 'alx-lisa-api:v1.0.0 (by /u/CaptainDiligent877)'}
    response = requests.get(url, params=params, headers=headers)

    data = {}

    if response.status_code == 200:
        data = response.json()['data']
    else:
        print("Invalid subreddit: {}".format(subreddit))
        return

    for post in data['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if " {} ".format(word.lower()) in " {} ".format(title):
                counts[word] = counts.get(word, 0) + 1

    after = data.get('after')
    count_words(subreddit, word_list, after, counts)
