from Classwork.mathplot.Library import float_values_manual_input, min_in_list

list, sum = float_values_manual_input()
average = sum/len(list)



min_, max_ = min_in_list(list)

print(list,average,sum, min_, max_)
