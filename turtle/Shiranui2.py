#thanks Shiranui 

from math import *
from kandinsky import *

def couleur():
  dr=c2[0]-c1[0]
  dg=c2[1]-c1[1]
  db=c2[2]-c1[2]
  return color(c1[0]+i*dr//320,c1[1]+i*dg//320,c1[2]+i*db//320)
  
c1=(255,255,0)
c2=(255,0,255)
for i in range(320):
  col=couleur()
  for j in range(222):
    set_pixel(i,j,col)
