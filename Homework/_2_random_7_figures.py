import random
def fig_from_range_gen():
    x = 0
    list = [[],[],[],[],[],[],[]]
    index = 0
    counter = 0
    while counter < 7:
        for i in list:
            i = random.randint(0, 9)
            list[index] =i
            index +=1
            counter +=1
    return list
list = fig_from_range_gen()
print(list)

