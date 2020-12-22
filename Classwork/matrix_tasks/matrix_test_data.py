def get_matrix_2x3():
    return [
        [1, 2, 3],
        [4, 5, 6]
    ]


def get_matrix_with_0_3x3():
    return [
        [0, 6, 2],
        [-5, 4, 0],
        [6, 0, -2]
    ]


def get_matrix_with_negative_3x3():
    return [
        [-1, 0, -3],
        [0, 9, 6],
        [4, -5, 6]
    ]


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