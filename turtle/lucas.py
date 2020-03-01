#Random Turtle drawing by Lucas

#Modules

import random
import math #needed for using square root for example
import turtle #needed for drawing purposes

#Variables
t = 0
T = 1000
x = 0 #x-coordinate
y = 0 #y-coordinate
z = 1 #scale
zz = 1
c = 0 #dont touch, for looping
d = random.random()*5
a = 300
angle1 = 0
margin = 5
turtle.pensize(1)
turtle.pencolor("red")

dd = []

print(d)

#Part 3

turtle.penup()
turtle.setpos(0*z,0*z)
turtle.pendown()
for t in range(0, T): #loops untill the max amount of coordinates are made
    turtle.speed(0) #speeds up the process

    x = math.cos(t*d)*z*zz
    y = math.sin(t*d)*z*zz

    t += 000.1
    z += 1.5
    dist1 = math.sqrt(x**2+y**2)
    if (dist1 <= a):
      turtle.goto(x,y)
    x += 0.0001
    angle1 = math.degrees(math.atan(y/x))
    DistAng = dist1,angle1
    dd.append(DistAng) #adds position to list

    if (t==T):
      print ("Drawing complete!")
    else:
      progress = str(int(t/T*100))
      print(progress+"%")
