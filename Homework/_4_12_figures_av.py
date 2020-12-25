from Classwork.mathplot.Library import min_in_list


def float_values_manual_input():
    counter_y = 0
    index = 0
    quantity_of_points = 20 #int(input("Введите количество значений: "))
    y_coord = [0]
    y_coord = y_coord * quantity_of_points
    sum = 0
    while counter_y < quantity_of_points:
        for value in y_coord:
            i = float(input("Введите значения: "))
            counter_y += 1
            y_coord[index] = i
            index += 1
            sum +=i
    return y_coord,sum

list, sum = float_values_manual_input()

min_, max_ = min_in_list(list)
average = sum/len(list)
print(list, sum, min_, max_, average)
