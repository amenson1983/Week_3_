
from Classwork.matrix_tasks.matrix_test_data import *

def get_count_column_with_zero(matrix):
    zero_count = 0
    for item in matrix:
        for j in item:
            if j == 0:
                zero_count += 1
    return zero_count


matrix = get_matrix_with_negative_3x3()
print("In matrix :",matrix)
zero_count = get_count_column_with_zero(matrix)
print("We have ", zero_count, "zeroes!")
zeroes_posit = []
for item in matrix:
    for j in item:
        x = item.index(0)
    zeroes_posit.append(x)
print("Their positions: ", zeroes_posit)


