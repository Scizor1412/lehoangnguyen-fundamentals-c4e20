from random import *
numbers = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
number = int(input("Enter a number? "))
count = 0
for value in numbers:
    if value == number:
        count +=1
print (count)