#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == None or len(matrix) == 0:
        return None
    return [[e * e for e in l] for l in matrix]
