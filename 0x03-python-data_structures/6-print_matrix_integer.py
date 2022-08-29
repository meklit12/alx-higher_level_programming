#!/usr/bin/python3
"""
removes all characters c and C from a string
"""


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != len(matrix[i]) - 1:
                    print(" ", end="")
            print("")
