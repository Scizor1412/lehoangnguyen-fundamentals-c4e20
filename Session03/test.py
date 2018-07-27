#Bai 1 
#count = 0
# loop=True
# while loop:
#     print ("Running...")
#     count += 1
#     if count ==5:
#         # loop = False
#         break
#         print ("Bye")
#Bai 2
from random import *
n = randint (0, 100)
count = 0
while True:
    guess = int (input("Guess my number (1-100): "))
    if guess < n:
        print ("too small")
    if guess >n:
        print ("too large")
    if guess == n:
        print ("Bingo")
        break
    count += 1
    if count > 6:
        print ("You lose")
        break