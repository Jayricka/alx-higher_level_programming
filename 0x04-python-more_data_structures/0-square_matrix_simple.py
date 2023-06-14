#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            # Square each value and add it to the new row
            new_row.append(num ** 2)
        # Add the new row to the new matrix
        new_matrix.append(new_row)
    return new_matrix
