#!/usr/bin/python3

class Square:
    """
    This is a class that represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance with an optional size.
        area(self): Calculates and returns the current square area.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.

    Raises:
        TypeError: If the given size is not an integer.
        ValueError: If the given size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the given size is not an integer.
            ValueError: If the given size is less than 0.
        """
        self.size = size

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the given size is not an integer.
            ValueError: If the given size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
