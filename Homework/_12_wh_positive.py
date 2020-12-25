from Classwork.exception.data_verify import input_positive, input_int_value

x = input_int_value()
x = input_positive(x)

list = list(range(2,x+1))

def _if_simple_fig(x):
    simple = False
    for i in range(2,x):

        y = x % i
        if y != 0:
            simple = True
        else: simple = False
        return simple

def list_of_simple(list,x):
    l_o_s = [] * x
    for item in list:
        simple = _if_simple_fig(item)
        if simple == True:
            l_o_s.append(item)
    return l_o_s


l_o_s = list_of_simple(list,x)
print(x,l_o_s)