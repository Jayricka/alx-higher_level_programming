#!/usr/bin/python3
"""Defines an inherited list class Mylist. """


class MyList(list):
    """A custom list class that inherits from the built-in list class."""


    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        sorted_list = sorted(self)
        print(sorted_list)
