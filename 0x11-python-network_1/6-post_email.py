#!/usr/bin/python3
"""
A script that:
- Takes in a URL,
- Sends a request to the URL, and
- Displays value of X-Request-Id variable found in header of response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
