lis_tot = list(range(30))
list_nchet = []
counter_ch = 0
if counter_ch < 10:
    for i in lis_tot:
        x = i%2
        if x == 1:
            list_nchet.append(i)
print(list_nchet)