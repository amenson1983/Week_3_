import Classwork
from Classwork import exception
from Classwork.exception import *
from Classwork.exception.data_verify import input_int_value


def print_v1(matrix):
    for irow in matrix:
        for ijcol in irow:
            print(ijcol, end="\t")
        print()

def print_v2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def get_matrix_from_console():
    matrix = []
    print("Enter number row")
    mrow = input_int_value()
    print("Enter number collumn")
    ncol = input_int_value()
    for i in range(mrow):
        matrix.append([])
        for j in range(ncol):
            print("Enter matrix[", i,"][",j,"]=")
            matrix[i].append(input_int_value())
    return matrix

def summarize_elements(matrix):
    sum_1 = 0
    for i in matrix:
        sum_1 += i
    return sum_1

def return_positive_elem(matrix):
    list__ = []
    for row in matrix:
        if row >= 0:
           list__.append(row)
        else:
            print("")
    return list__

def return_even_elem(matrix):
    list__ = []
    for item in matrix:
        x = item%2
        if x == 0:
            list__.append(item)
        else: print("")
    return list__