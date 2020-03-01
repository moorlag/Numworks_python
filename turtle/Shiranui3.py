#Thanks Shiranui

from kandinsky import*
from math import*

def cercle(x0,y0,r,c,e):
  for i in range(2*e):
    xd=x0-int((r-i*0.5)/sqrt(2))
    xf=x0+int((r-i*0.5)/sqrt(2))
    for x in range(xd,xf+1):
      x1=x
      y1=y0+int(sqrt((r-i*0.5)**2-(x-x0)**2))
      set_pixel(x,y1,c)
      for j in range(3):
        x2=x0+y1-y0
        y2=y0+x0-x1
        set_pixel(x2,y2,c)
        x1,y1=x2,y2
        
def rosace(n,r,c,e):
  x,y=160+r,111
  for i in range(n):
    x1=int(160+r*cos(i*2*pi/n))
    y1=int(111+r*sin(i*2*pi/n))
    cercle(x1,y1,r,c,e)
    
cint=color(205,50,123)
cbor=color(0,0,0)
rosace(12,20,cint,1)
