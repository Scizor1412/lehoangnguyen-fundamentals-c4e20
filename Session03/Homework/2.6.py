from random import * 
flock = [randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300)]
print ("Hello, my name is Nguyen and these are my sheeps' sizes")
print (flock)
n = int (input ("How long are you going to be a shepherd (months): "))
for i in range (1, n+1):
    print ("Month ", i, ":", sep="")
    if i == 1:
        print ("One month has passed, now here is my flock")
    else:
        print ("Another month has passed, now here is my flock")
    flock = [x+50 for x in flock]
    print (flock)
    if i != n:
        print ("Now my biggest sheep has size ", max(flock), ". Let's shear it.", sep = "")
        print ("After shearing, here is my flock")
        max_index = flock.index(max(flock))
        flock [max_index] = 8
        print (flock)
    else:
        total_size = 0
        for j in range (len(flock)):
            total_size = total_size + flock [j]
        print ("My flock has total size of:", total_size)
        print ("I would get", total_size, "* 1000 =", total_size*1000)