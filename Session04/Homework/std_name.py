wrong_name= input ("Full Name: ").lower()
print (wrong_name)
name= wrong_name.split()
for i in range (len(name)):
    name[i].replace(" ", "")
right_name=" ".join(name)
print ((right_name).title())