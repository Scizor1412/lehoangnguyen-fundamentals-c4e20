from turtle import *
speed(-1)
shape ("turtle")
color ("blue")

socanh=int(input("Nhap vao 1 so"))
for i in range(socanh):
    forward (2)
    left (360/(socanh))
mainloop()