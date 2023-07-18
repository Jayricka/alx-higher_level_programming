#!/usr/bin/python3
"""This function contains the definition of the Base class."""


class Base:
    """Base class for managing the id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): The id value for the instance. If None, a unique id will be assigned.

        Attributes:
            id (int): The id value of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
