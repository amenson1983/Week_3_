from Classwork.exception.data_verify import input_int_value
from Classwork.mathplot.Library import float_values_manual_input_, int_values_manual_input_
def more_than(list):
    index_ = 0
    n = int(input("Point the N number:"))
    new_list = []
    shit = []
    new_list = new_list * len(list)
    for i in list:
        if i >= n:
            new_list.append(i)
            index_ +=1
        elif i < n:
            shit.append(i)
            index_ +=1
    return new_list


list, sum = int_values_manual_input_()

new_list = more_than(list)
#print(list)
print(new_list)
