teen_code_dict = {
    "hc" : "hoc",
    "ng" : "nguoi",
    "pt" : "party",
    "eny" : "em nguoi yeu",
    "any": "anh nguoi yeu",
    "ns": "noi",
    "ngta": "nguoi ta",
    "lm": "lam",
    "r" : "ulti",
    "stt": "status"
}
print ("***************************************************")
for key in teen_code_dict.keys():
    print (key, end="\t")
print ("")
while True:
    code = input ("Your code: ")
    if code in teen_code_dict:
        print ("Translation:",teen_code_dict[code])
        cont = input ("Do you want to continue? (Y/N)? ")
        if cont.lower() == "y":
            continue
        else:
            break
    else:
        ans = input ("Not found, do you want to contribute this word? (Y/N)?")
        if ans.lower() == "y":
            meaning = input ("Enter your translation: ")
            print ("Updated")
            print ("***************************************************")
            teen_code_dict[code] = meaning
            for key in teen_code_dict.keys():
                print (key, end = "\t")
            print ("")
            cont = input ("Do you want to continue? (Y/N)? ")
            if cont.lower() == "y":
                continue
            else:
                break