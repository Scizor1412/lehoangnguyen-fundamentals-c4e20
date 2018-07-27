from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]
for i in range (0, 5):
    color (colors[i])
    begin_fill()
    for j in range (4):
        if j %2 ==1:
            forward (100)
        else:
            forward (50)
        left (90)
    end_fill()
    forward (50)
mainloop()