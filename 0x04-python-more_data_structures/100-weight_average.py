#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0
    weighted_sum = 0  # Initialize the weighted sum
    total_weight = 0  # Initialize the total weight
    for score, weight in my_list:
        weighted_sum += score * weight
        total_weight += weight
    return weighted_sum / total_weight
