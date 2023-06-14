#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_nums = set(my_list)  # Create a set to store unique integers
    total = 0

    for num in unique_nums:
        total += num

    return total
