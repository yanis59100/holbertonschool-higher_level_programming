#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        new_list.append(list(sub_matrix))
    return new_list
