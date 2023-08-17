#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    values_at_index_0 = []
    values_at_index_1 = []
    values_at_index_2 = []

    for inner_list in reversed(matrix):
        values_at_index_0.append(inner_list[0])
        values_at_index_1.append(inner_list[1])
        values_at_index_2.append(inner_list[2])

    rotated_list = [values_at_index_0, values_at_index_1, values_at_index_2]
    print(rotated_list)
