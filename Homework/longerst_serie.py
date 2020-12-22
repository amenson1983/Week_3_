#6. Вывести номер строки, в которой находится
# самая длинная серия одинаковых элементов.
from Classwork.matrix_tasks.matrix_test_data import get_matrix_with_0_3x3

matrix = get_matrix_with_0_3x3()
count_max = len(matrix) - 1
count_min = 0
lenth_1 = 0
lenth_2 = 0
lenth_3 = 0
x = matrix[0]
y = matrix[1]
w = matrix[2]

for i in x:
    x.count(i)
    if x.count(i) > 1:
        lenth_1 +=1
print("",lenth_1, x)
for i in y:
    y.count(i)
    if y.count(i) > 1:
        lenth_2 +=1
print("\n" ,lenth_2, y)
for i in w:
    w.count(i)
    if w.count(i) > 1:
        lenth_2 +=1
print("\n" ,lenth_3, w)

if lenth_1>lenth_2 and lenth_1>lenth_3:
    print("Longest position is 0", x)
elif lenth_2>lenth_1 and lenth_2>lenth_3:
    print("Longest position is 1", y)
else: print("Longest position is 2", z)