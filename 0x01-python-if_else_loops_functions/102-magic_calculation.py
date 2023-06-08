#!/usr/bin/python3


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < c:
        return (b)
    if b > c:
        return (a + c)
    return (a*b - b)
