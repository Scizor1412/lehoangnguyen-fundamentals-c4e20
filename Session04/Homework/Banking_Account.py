balance = input("Enter your balance: ")
outstanding = list(balance)
print (outstanding)
while outstanding[0] == "0":
    del outstanding[0]
for i in range (len(outstanding)-3, 0, -3):
    outstanding.insert(i, ",")
print ("Your bank account have: $",*outstanding, sep ="", end ="")