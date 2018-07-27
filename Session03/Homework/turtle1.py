from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]
for j in range (3, len(colors)+3):
    color (colors[j-3])
    for i in range (j):
        forward (100)
        left (360/(j))
mainloop()