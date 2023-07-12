#!/usr/bin/python3
"""Defines Mylist class"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    Public instance method:
        - print_sorted(): Prints the list in sorted (ascending) order.

    Inherits from:
        list
    """

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        sorted_list = sorted(self)
        print(sorted_list)
