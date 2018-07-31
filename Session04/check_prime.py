# n = int (input ("Enter a number: "))
# count = 0
# for i in range (1,n):
#     if n%i == 0:
#         count +=1
# if count > 1:
#     print ("n is not a prime number.")
# else:
#     print ("n is a prime number.")

n = int (input ("Enter a number: "))
is_prime=True
i=2

while i<=n **(1/2):
    if n%i == 0:
        is_prime=False
        break
    i+=1

if is_prime:
    print ("{} is a prime number".format(n))
else:
    print ("{} is not a prime number".format(n))