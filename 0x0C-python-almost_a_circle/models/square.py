#!/usr/bin/python3

"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Assigns attributes to the instance"""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
