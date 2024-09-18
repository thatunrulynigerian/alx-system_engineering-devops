#!/usr/bin/python3
"""
Script to query and retrieve all hot posts from a specified Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], pagination_token=""):
    """
    Recursively retrieves a list of titles of all hot posts
    from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        pagination_token (str, optional): Token used for pagination.
                                           Default is an empty string.

    Returns:
        list: A list of post titles from the hot section of the subreddit, or None if subreddit is invalid.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "my_reddit_app:v1.0.0 (by /u/your_username)"  # Change this to your Reddit username
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "after": pagination_token,
        "limit": 100
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Handle errors gracefully
    if response.status_code == 404:
        return None
    elif response.status_code != 200:
        return None

    # Parse the JSON response and extract relevant data
    results = response.json().get("data")
    pagination_token = results.get("after")

    # Append post titles to the hot_list
    for post in results.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    # If there are more posts to retrieve, recursively call the function
    if pagination_token is not None:
        return recurse(subreddit, hot_list, pagination_token)

    # Return the final list of hot post titles
    return hot_list

# Example usage
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    titles = recurse(subreddit)
    if titles is not None:
        print(f"Hot posts in r/{subreddit}:")
        for title in titles:
            print(f"- {title}")
