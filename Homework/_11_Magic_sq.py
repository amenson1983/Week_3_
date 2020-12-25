from Classwork.exception.data_verify import input_int_value, input_mark
import random

from Classwork.mathplot.Library import create_matrix

list = create_matrix() #genereted matrix
#list = [[4,9,2],[3,5,7],[8,1,6]] #Magic matrix
lengh = len(list)
for i in list:
    sum_str_1 = sum(list[0])
    sum_str_2 = sum(list[1])
    sum_str_3 = sum(list[2])

sum_col_1 = 0
sum_col_2 = 0
sum_col_3 = 0
for i in range(0,lengh):
    sum_col_1 += list[i][0] #sum_col_1 = list[0][0]+list[1][0]+list[2][0]
    sum_col_2 += list[i][1] #sum_col_2 = list[0][1]+list[1][1]+list[2][1]
    sum_col_3 += list[i][2] #sum_col_3 = list[0][2]+list[1][2]+list[2][2]
diag_1 = list[0][0]+list[1][1]+list[2][2]
diag_2 = list[2][0]+list[1][1]+list[0][2]
if sum_col_1 == sum_col_2 == sum_col_3 == sum_str_1 == sum_str_2 == sum_str_3 == diag_1 == diag_2:
    print("BINGO!!!")
else: print("Regular matrix")
#print(list, sum_str_1, sum_str_2, sum_str_3, sum_col_1,sum_col_2,sum_col_3,diag_1,diag_2)