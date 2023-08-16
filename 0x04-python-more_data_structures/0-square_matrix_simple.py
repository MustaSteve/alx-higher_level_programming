#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squere_marix = []
    for i in matrix:
        inside = list(map(lambda x: x**2, i))
        squere_marix.append(inside)
    return squere_marix
