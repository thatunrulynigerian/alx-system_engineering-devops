#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0
    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }
    
    # Make the GET request without allowing redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    # Parse the JSON response
    data = response.json()
    subs = data.get("data", {}).get("subscribers", 0)
    return subs
