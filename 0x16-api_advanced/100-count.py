#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests

def count_words(subreddit, keywords, after=None, word_counts={}):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.
    
    Args:
        subreddit (str): The name of the subreddit.
        keywords (list): List of keywords to count.
        after (str, optional): Token for pagination.
        word_counts (dict, optional): Dictionary to hold counts of each keyword.
    """
    if not keywords or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data["data"]["children"]

    for post in posts:
        title = post["data"]["title"].lower()
        for keyword in keywords:
            # Only count if the keyword is not part of another word
            if f" {keyword.lower()} " in f" {title} ":
                word_counts[keyword] = word_counts.get(keyword, 0) + title.count(keyword.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, keywords, after, word_counts)
    else:
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word.lower()}: {count}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
