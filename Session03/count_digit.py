# n = float(input("Enter a number: "))
# count = 0
# while True:
#     if n >= 1:
#         count +=1
#         n = n/10
#     else:
#         print (count)
#         break
n = int (input("Enter a number: "))
count = 0
while n!=0:
    n=n//10
    count +=1
print (count)