menu=["Cơm", "Cá", "Thịt bò", "Ghẹ", "Pizza", "Gà ở Trần Duy Hưng"]
#separator
# print (len(menu))
# menu.append ("Ghẹ")
# print (len(menu))
# for i in range (len(menu)):
#     print (menu[i])

# for index, item in enumerate(menu):
#     print ("{}. {}".format(index +1, item))
# for item in menu:
#     print (item)

#update
print (*menu, sep=", ")
menu[4] = "Tôm hùm"
print (*menu, sep=", ")