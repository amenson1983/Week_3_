from Classwork.matrix_tasks.matrix_test_data import get_matrix_with_negative_3x3, get_strings_less_zero

# 5. Вывести максимальное из чисел,
# встречающихся в заданной матрице более одного раза.

matrix = get_matrix_with_negative_3x3()
list_ = []
for i in matrix:
    list_ += i

max_ = list_[0]
new_list = []
count = 1
for i in list_:
    if list_.count(i) >=2:
       new_list.append(i)
    else: list_.remove(i)

print("\nМаксимальное из чисел,встречающихся в заданной матрице более одного раза: ", new_list)
