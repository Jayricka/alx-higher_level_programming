#!/usr/bin/python3

"""This module defines the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the Square instance.
        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

