# print ("Guess your number game")
# alsksdjaskdjhd = input ("Think of a number between 0-100. Then press 'Enter'")
# print ("'c' if my guess is correct")
# print ("'s' if my guess is smaller than your number.")
# print ("'l' if my guess is larger than your number.")
# low = 0
# high = 100
# mid = (low + high)/2
# ans = input ("Is {} your number?".format(mid))
# if ans != "c":
#     if ans == "s":
#         low = mid
#     elif ans == "l":
#         high = mid
#     mid = (low + high)//2
#     ans = input ("Is {} your number?".format(mid))
# else:
#     print ("Hura")
print ("Guess your number game")
print ("Now think of a number (0-100), then press 'Enter'")
input()

print ("""
All you have to do is to answer to my guess
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number
""")
low = 0
high = 100
playing = True
while playing:
    mid = (low +high)//2
    guess = input ("Is {} your number?".format(mid))
    if guess == "c":
        print ("I knew it")
        playing = False
    elif guess == 's':
        low = mid
    elif guess == 'l':
        high = mid
    else:
        print ("Wrong answer. Fuck you!!!")
    if high == low:
        print ("Fuck you!!! Cheater.")
        break