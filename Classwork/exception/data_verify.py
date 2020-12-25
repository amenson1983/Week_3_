def input_int_value():
    while True:
        try:
            value = int(input("Enter int value"))
            break
        except:
            print("Not int, try again")
    return value

def input_mark():
    while True:
        print("enter mark (1<mark<=9)")
        mark = input_int_value()
        if 1 < mark <= 9:
            return mark
        else:
            print("Value not mark, try again")

def input_float_value():
    while True:
        try:
            value = float(input("Enter float value"))
            break
        except:
            print("Not float, try again")
    return value

def input_positive(mark):
    while True:

        if 1 < mark:
            return mark
        else:
            print("Value not mark, try again")