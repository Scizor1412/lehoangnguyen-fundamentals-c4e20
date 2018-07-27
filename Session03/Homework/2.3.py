from random import * 
flock = [randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300),randint(1,300)]
print ("Hello, my name is Nguyen and these are my sheeps' sizes")
print ("Now my biggest sheep has size ", max(flock), ". Let's shear it.", sep = "")
max_index = flock.index(max(flock))
flock [max_index] = 8
print ("After shearing, here is my flock")
print (flock)