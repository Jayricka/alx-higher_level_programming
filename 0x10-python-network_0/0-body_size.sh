#!/bin/bash
# This script takes a URL as an argument, sends a cURL request, and displays the body size in bytes.

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a cURL request silently and retrieve the content length if available
content_length=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')

# If content length is not found, set it to 0
if [ -z "$content_length" ]; then
    content_length=0
fi

# Output the content length only
echo "$content_length"

