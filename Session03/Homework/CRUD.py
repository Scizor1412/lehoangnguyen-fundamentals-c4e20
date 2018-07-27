clothes = ["T-Shirt", "Sweater"]
while True:
    rep= input ("Welcome to our shop, what do you want (C, R, U, D)? ")
    if rep not in ("C", "R", "U", "D"):
        print ("The answer must be Uppercase of C, R, U, or D.")
        print ("Please try again. ")
    elif rep == "R":
        print ("Our items: ", end= "")
        print (*clothes, sep =", ")
    elif rep == "C":
        new_clothes = input("Enter new item: ")
        while new_clothes != "Jeans":
            print ("BTVN bảo chỉ được thêm Jeans thôi.")
            new_clothes = input("Enter new item: ")
        clothes.append (new_clothes)
        print (*clothes, sep=", ")
    elif rep == "U":
        n = int (input ("Update position: "))
        while n !=2:
            print ("Xem lại đề bài đi nhé -_-")
            n = int (input ("Update position: "))
        new_clothes_2 = input("New item? ")
        while new_clothes_2 != "Skirt":
            print ("Có biết chữ không thế -_-")
            new_clothes_2 = input("New item? ")
        clothes [n-1] = "Skirt"
        print (*clothes, sep=", ")
    elif rep == "D":
        n = int (input("Delete position? "))
        while n != 3:
            print ("Pleaseeeeee, đọc lại đề đi :((")
            n = int (input("Delete position?"))
        del clothes [n-1]
        print (*clothes, sep=", ")
        break