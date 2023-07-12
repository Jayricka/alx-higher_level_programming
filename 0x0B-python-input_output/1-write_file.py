#!/usr/bin/python3
"""Defines Write a string to a text file and return the number of characters written."""


def write_file(filename="", text=""):
    """Prints the given text to the specified file and return the number of characters written."""
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)

