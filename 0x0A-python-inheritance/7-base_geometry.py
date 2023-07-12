#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculate the area.
        
        Raises:
            Exception: If the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.
        
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

