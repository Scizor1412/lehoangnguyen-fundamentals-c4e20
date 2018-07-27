danhsach = ["phim", "game", "sleep"]
print ("Hi there, here your favorite things so far")
print (*danhsach, sep=", ")
them = input ("Ban muon them gi khong? ")
danhsach.append (them)
print (*danhsach, sep=", ")