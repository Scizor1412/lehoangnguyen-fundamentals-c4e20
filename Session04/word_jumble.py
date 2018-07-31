from random import *
words = ["champion", "scizor", "nguyen"]
word = choice(words)
chars = list (word)
question = []

while len(chars) !=0:
    char = choice(chars)
    chars.remove(char)
    question.append(char)

print (*question, sep = " ")
answer = input ("Nhập đáp án: ")

if answer == word:
    print ("You win")

else: print ("Wrong answer")