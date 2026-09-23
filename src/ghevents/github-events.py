#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv("GITHUB_USER")
url = f"https://api.github.com/users/{GHUSER}/events"


def retrieve_events(url):
    """Get GitHub events."""
    response = requests.get(url).text
    return json.loads(response)


def print_events(events, n=5):
    """Print the first n GitHub events."""
    for x in events[:n]:
        event = x["type"] + " :: " + x["repo"]["name"]
        print(event)


def main():
    """Get and print GitHub events."""
    print(GHUSER)
    print(url)

    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()
    
