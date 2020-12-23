import matplotlib.pyplot as plt
import random


def OX_values_input_manual():
    return OX_values_manual_input()


def OX_values_manual_input():
        counter_x = 0
        index = 0
        quantity_of_points = int(input("Введите количество значений: "))
        x_coord = [0]
        x_coord = x_coord * quantity_of_points
        while counter_x < quantity_of_points:
            for value in x_coord:
                i = float(input("Введите значения оси Х: "))
                counter_x += 1
                x_coord[index] = i
                index += 1
        return x_coord


def OY_values_manual_input():
    return OY_values_manual_input()


def OY_values_manual_input():
    counter_y = 0
    index = 0
    quantity_of_points = int(input("Введите количество значений: "))
    y_coord = [0]
    y_coord = y_coord * quantity_of_points
    while counter_y < quantity_of_points:
        for value in y_coord:
            i = float(input("Введите значения оси Y: "))
            counter_y += 1
            y_coord[index] = i
            index += 1
    return y_coord


def linear_diagram(x_coord,y_coord):
    linear_diagram(x_coord, y_coord)


def linear_diagram(x_coord, y_coord):
    x_min = min(x_coord)
    x_max = max(x_coord)
    y_min = min(y_coord)
    y_max = max(y_coord)
    plt.plot(x_coord, y_coord, marker="s")
    plt.title(input("Введите заголовок диаграммы: "))
    plt.xlabel(input("Введите подпись по оси ОХ: "))
    plt.ylabel(input("Введите подпись по оси ОY: "))
    plt.xlim(xmin=x_min-1, xmax=x_max+1)
    plt.ylim(ymin=y_min-1, ymax=y_max+1)
    plt.grid(True)
    plt.show()

