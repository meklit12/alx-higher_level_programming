#!/usr/bin/python3
"""
square matrix map
"""


def square_matrix_map(matrix=[]):
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
