#!/usr/bin/python3

"""This module defines the BaseGeometry class."""

class BaseGeometry:
    """BaseGeometry is a base class for geometric shapes."""

    def area(self):
        """Computes the area of the geometric shape.
        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

