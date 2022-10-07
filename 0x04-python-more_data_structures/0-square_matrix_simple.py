#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix2.append((matrix[x][y]**2))
    
    return matrix2