#7. Характеристикой строки целочисленной матрицы
# назовем сумму ее положительных четных элементов.
#    Переставляя строки заданной матрицы,
# расположить их в соответствии с ростом характеристик.
from Classwork.matrix_tasks.matrix_helper import return_positive_elem, return_even_elem, summarize_elements
from Classwork.matrix_tasks.matrix_test_data import get_matrix_with_0_3x3

matrix = get_matrix_with_0_3x3()
new_list = []
final_list = [[],[],[]]
list_1 = matrix[0]
list_2 = matrix[1]
list_3 = matrix[2]
ch_1 = []
ch_2 = []
ch_3 = []
ch_1 = return_positive_elem(list_1)
ch_2 = return_positive_elem(list_2)
ch_3 = return_positive_elem(list_3)
ch_1 = return_even_elem(ch_1)
ch_2 = return_even_elem(ch_2)
ch_3 = return_even_elem(ch_3)
ch_1 = summarize_elements(ch_1)
ch_2 = summarize_elements(ch_2)
ch_3 = summarize_elements(ch_3)
new_list = [ch_1,ch_2,ch_3]

def sorting(matrix):
    new_list.sort()
    return new_list


new_list = sorting(new_list)

if new_list.index(ch_1) == 0:
    final_list[0] = list_1
elif new_list.index(ch_1) == 1:
    final_list[1] = list_1
elif new_list.index(ch_1) == 2:
    final_list[2] = list_1

if new_list.index(ch_2) == 0:
    final_list[0] = list_2
elif new_list.index(ch_2) == 1:
    final_list[1] = list_2
elif new_list.index(ch_2) == 2:
    final_list[2] = list_2

if new_list.index(ch_3) == 0:
    final_list[0] = list_3
elif new_list.index(ch_3) == 1:
    final_list[1] = list_3
elif new_list.index(ch_3) == 2:
    final_list[2] = list_3


print(final_list)