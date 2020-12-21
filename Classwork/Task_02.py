list_ch = []
list_nchet = []
x = 0
y = 0
for i in range(1,11,1):
    ch_input = int(input("Input value"))
    ch_def = ch_input%2
    if ch_def == 0:
       list_ch.append(i)
       y+=1
    else: list_nchet.append(i)

print(list_ch, "\n", list_nchet)
print ("Четных: ", len(list_ch), "Нечетных: ", len(list_nchet))