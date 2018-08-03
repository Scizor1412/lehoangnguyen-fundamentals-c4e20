number = int (input("How many B bacterias are there? "))
time = int (input ("How much time in minutes will we wait? "))
bacterias = number * (2**(time//2))
print ("After {} minutes, we would have {} bacterias.".format(time, bacterias))