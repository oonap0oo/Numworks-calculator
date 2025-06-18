import kandinsky
from math import *
# draw a line between any twon points
def connect(x1,y1,x2,y2,co="black"):
  xspan=x2-x1;yspan=y2-y1
  steps=max(abs(xspan),abs(yspan))
  if steps==0:
    kandinsky.set_pixel(x1,y1,co)
    return
  dx=xspan/steps;dy=yspan/steps
  x=x1;y=y1
  for k in range(steps):
    kandinsky.set_pixel(int(x+.5),int(y+.5),co)
    x+=dx;y+=dy
# draw the star
def drawstar(x,y,n,r):
  col=("red","green","blue")
  xx=[];yy=[]
  for k in range(n):
    angle=k/n*2*pi
    xx.append(int(r*cos(angle)+x))
    yy.append(int(r*sin(angle)+y))
  for k in range(n):
    for m in range(k,n):
      c=col[m%3]
      connect(xx[k],yy[k],xx[m],yy[m],c)

kandinsky.fill_rect(0,0,320,230,"black")

drawstar(160,110,20,105)






