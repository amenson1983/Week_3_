def weekdays_sales_input():
    counter_y = 0
    index = 0
    gross_sales = 0
    daily_sales = [[],[],[],[],[],[],[]]
    while counter_y < 7:
        for value in daily_sales:
            i = float(input("Введите продажи за день"))
            counter_y += 1
            daily_sales[index] = i
            index += 1
            gross_sales += i
    return daily_sales, gross_sales

daily_sales,gross_sales = weekdays_sales_input()
print(daily_sales,"\n",gross_sales)