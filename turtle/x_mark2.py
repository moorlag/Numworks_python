from turtle import *

speed(10)
penup()
goto(-160,110)
pendown()
x = 320
y = 220


for i in range(45):
  forward(x)
  right(90)
  forward(y)
  right(90)
  x = x - 5
  y = y - 5
