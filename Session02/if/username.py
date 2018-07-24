from getpass import *
print ("Hi there, this is the Pokemon World")
Username = input ("Username:")
if Username == "Scizor":
    Password = getpass ("Password:")
    if Password == "Scizor":
        print ("Welcome", Username,"!")
    else:
        print ("Password Incorrect")
else:
    print ("Wrong username")