#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) <= 0:
        return None
    return [[e * e for e in line] for line in matrix]
