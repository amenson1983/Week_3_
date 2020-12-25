from Classwork.mathplot.Library import float_values_manual_input

list, sum = float_values_manual_input()
average = sum/len(list)
def min_in_list(list):
    min_ = list[0]
    max_ = list[0]
    length = len(list)
    index = 0
    for i in list:
        if i <min_:
            min_ = i
        if i >max_:
            max_ = i
    return min_, max_


min_, max_ = min_in_list(list)

print(list,average,sum, min_, max_)
