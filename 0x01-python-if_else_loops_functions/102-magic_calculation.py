#!/usr/bin/python3
# Author - Jayricka

def magic_calculation(a, b, c):
    """Perform the same computation as the provided bytecode."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
