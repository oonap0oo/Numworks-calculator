# Gingerbread man fractal
import kandinsky
from math import *

def dist(x1,y1,x2,y2):
  return sqrt((x1-x2)**2+(y1-y2)**2)

def drawgingerbread(N=50000):
  kandinsky.fill_rect(0,0,320,230,"black")
  x,y=-0.1,0
  for _ in range(N):
    xold,yold=x,y
    x,y=1-y+abs(x),x
    #print((x-xold)**2+(y-yold)**2)
    xscr=int(300*(x+3.5)/12)
    yscr=int(210*(9.5-y)/12)
    c=int(dist(x,y,xold,yold)/12*512)
    g=(c % 32)*8+7
    b=(c % 256)
    r=(c % 128)*2+1
    kandinsky.set_pixel(xscr,yscr,kandinsky.color(r,g,b))
  kandinsky.draw_string("Gingerbread man fractal",10,2,"green","black")

drawgingerbread()
