#!/bin/bash
# This script takes a URL as an argument, sends a cURL request, and displays the body size in bytes.
curl -s "$1" | wc -c
