#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    leng = 0
    for i in range(len(matrix)):
        if type(matrix[i]) is not list or matrix[i] == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if i == 0:
            leng = len(matrix[i])
        elif leng != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_r = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        matrix_r.append(row)
    return matrix_r
