from Classwork.matrix_tasks.matrix_test_data import get_matrix_with_negative_3x3


def get_strings_less_zero(matrix):
    negative_list_uniq = []
    negative_indicate = False
    negative_count = 0
    negative_list = []
    for item in matrix:
        for cell in item:
            if cell < 0:
                negative_indicate = True
                negative_list.append(matrix.index(item))
                negative_count += 1
            else:
                negative_indicate = False
    ind = 0
    for item in negative_list:
        if ind > item:
            print("")
        else:
            negative_list_uniq.append(item)
        ind += 1
    return negative_count, negative_list_uniq
