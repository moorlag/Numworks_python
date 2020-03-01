from turtle import *

speed(50)
penup()
goto(-160,110)
pendown()
x = 320
y = 220

for i in range(40):
  forward(x)
  right(90)
  forward(y)
  right(90)
  x = x - 20
  y = y - 20
