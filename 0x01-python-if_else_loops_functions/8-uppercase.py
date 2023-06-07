#!/usr/bin/python3

def uppercase(string):
    result = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
