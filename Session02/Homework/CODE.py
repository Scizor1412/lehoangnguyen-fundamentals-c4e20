n= int (input ("Enter a number: "))
#hangdau
print ("  ", end = "")
for i in range (n-1):
    print ("* ", end= "")
for i in range (n//2 +1):
    print ("  ", end= "")
for i in range (n-2):
    print ("* ", end="")
for i in range (n//2 +1):
    print ("  ", end="")
for i in range (n-1):
    print ("* ", end="")
for i in range (n//2 +1):
    print ("  ", end="")
for i in range (n):
    print ("* ", end="")
print ("")
#hethangdau
for j in range (n-2):
    
    print ("* ", end="")
    for i in range (n//2 + n -1):
        print ("  ", end="")
    print ("* ", end="")
    for i in range (n-2):
        print ("  ", end="")
    print ("* ", end="")
    for i in range (n//2):
        print ("  ", end="")
    print ("* ", end="")
    for i in range (n-2):
        print ("  ", end="")
    print ("* ", end="")
    for i in range (n//2):
        print ("  ", end="")
    if j == (n//2-1):
        for k in range (n-(n//3)):
            print ("* ", end ="")
    else:
        print ("* ", end="")
    print ("")
#hangcuoi
print ("  ", end = "")
for i in range (n-1):
    print ("* ", end= "")
for i in range (n//2 +1):
    print ("  ", end= "")
for i in range (n-2):
    print ("* ", end="")
for i in range (n//2 +1):
    print ("  ", end="")
for i in range (n-1):
    print ("* ", end="")
for i in range (n//2 +1):
    print ("  ", end="")
for i in range (n):
    print ("* ", end="")
#hethangcuoi