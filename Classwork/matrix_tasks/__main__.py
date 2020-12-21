from Classwork.matrix_tasks.matrix_helper import get_matrix_from_console
from Classwork.matrix_tasks.matrix_tasks import print_positive_elem

if __name__ == '__main__':
    matrix = None
    while True:
        print("0. Вывести данные с консоли")
        print("1. Вывести все положительные елементы")
        answer = int(input("Enter answer"))
        if answer == 0 :
            matrix = get_matrix_from_console()
        elif answer == 1:
            if matrix != None:
                print_positive_elem(matrix)





