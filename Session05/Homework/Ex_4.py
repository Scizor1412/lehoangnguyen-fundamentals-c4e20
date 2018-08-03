numb_month = [1, 1, "numb_month_1", "numb_month_2", "numb_month_3", "numb_month_4"]
for i in range (2, 6):
    numb_month[i] = numb_month[i-1] + numb_month[i-2]
for i in range (1, 6):
    print ("Month {}: {} pair(s) of rabbit".format(i-1, numb_month[i]))