#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __equalnot__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __notequal__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
