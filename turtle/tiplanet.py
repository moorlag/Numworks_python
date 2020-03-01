from turtle import *
def spiral(N_iteration):
  N_iteration *= 25
  for i in range(N_iteration):
# Change pen color
    gray=255-(i*255/N_iteration)
    pencolor(int(gray),int(gray*0.75),int(gray*0.25))
# Draw a segment of the spiral
    forward(i*0.1)
    left(10)
