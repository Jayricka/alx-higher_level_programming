#!/usr/bin/python3
import traceback

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError as error:
        print("\nIndexError: list index out of range\n")
        traceback.print_exc()
        raise error
    finally:
        print()
        return count
