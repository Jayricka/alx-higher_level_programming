#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
It displays the response body in a specific format.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
