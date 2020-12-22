from Classwork.matrix_tasks.matrix_test_data import get_matrix_with_negative_3x3



matrix = get_matrix_with_negative_3x3()
negative_list_copy = []
negative_list_uniq = []
negative_indicate = False
negative_count = 0
negative_list = []
for item in matrix:
    for cell in item:
        if cell < 0:
            negative_indicate = True
            negative_list.append(matrix.index(item))
            negative_count +=1
        else: negative_indicate = False

print ("Количество отрицательных элементов: ", negative_count, "\nПозиции строк: ", negative_list)