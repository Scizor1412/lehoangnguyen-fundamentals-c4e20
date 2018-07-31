print ("Welcome to the World of Pokemon")
count = 0
username = input ("Username: ")
while username != "Scizor":
    print ("Not you")
    count +=1
    if count == 3:
        print ("Getaway")
        break
    else:
        username = input ("Username: ")
else: 
    password = input ("Password: ")
    while password != "Scizor":
        print ("Wrong password")
        count +=1
        if count == 3:
            print ("Getaway")
            break
        else:
            password = input ("Password: ")
    else:
        print ("Welcome, ", username)

# print ("Welcome to the World of Pokemon")
# count = 0
# loop = True
# while loop:
#     username = input ("Username: ")
#     if username == "Scizor":
#         password = input ("Password: ")
#         if password == "Scizor":
#             print ("Welcome, Scizor")
#             break
#         else:
#             print ("Wrong password!")
#     else:
#         print ("Wrong username!")
#     count +=1
#     if count ==3:
#         print ("Getaway")
#         break