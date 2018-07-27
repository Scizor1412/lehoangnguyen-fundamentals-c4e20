menu = ["death note", "netflix", "teaching"]
print ("Hi there, here your favorite things so far")
print ("**********************************")
for index, item in enumerate(menu):
    print (index +1, item, sep =". ")
print ("**********************************")
n = int (input ("Position you want to update? "))
replace = input ("Your replacing favorite? ")
menu[n-1]=replace
print ("**********************************")
for index, item in enumerate(menu):
    print (index +1, item, sep =". ")
print ("**********************************")