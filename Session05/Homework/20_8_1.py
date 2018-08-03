import string
alphabet=list(string.ascii_lowercase)
sentence=list((input("Enter your sentence: ")).lower())
for i in alphabet:
    count = 0
    for j in sentence:
        if i == j:
            count +=1
    print ("{}\t {}". format(i, count))