#!/usr/bin/python3
"""Defines a text file and print its content to stdout."""


def read_file(filename=""):
    """Print the content of a text file and print it to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
