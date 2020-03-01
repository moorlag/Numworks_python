#Thanks Shiranui
from math import *
from kandinsky import *

def couleur():
  r=c1[0]+i*(c2[0]-c1[0])//320
  g=c1[1]+i*(c2[1]-c1[1])//320
  b=c1[2]+i*(c2[2]-c1[2])//320
  r+=j*(c3[0]-r)//320
  g+=j*(c3[1]-g)//320
  b+=j*(c3[2]-b)//320
  return color(r,g,b)
  
c1=(255,255,0)
c2=(255,0,255)
c3=(0,255,255)
for i in range(320):
  for j in range(222):
    col=couleur()
    set_pixel(i,j,col)
