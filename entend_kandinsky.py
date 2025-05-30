import kandinsky
from math import *

# function draws a line using kandinsky library
# start point:(x1,y1), end point:(x2,y2)
# optionally color can be specified
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

# function draws a circle using the Minksy circle algoritm
# center of circle: (xc,yc), radius: r
# optionally color can be specified
def circle(xc,yc,r,co="black"):
  N=max(2*r,200)
  fr=N/(2*pi)
  x=r; y=0
  xold=x+xc; yold=y+yc
  for k in range(N):
    x-=y/fr;y+=x/fr
    xscr=int(x+xc+.5); yscr=int(y+yc+.5)
    connect(xscr,yscr,xold,yold,co)
    xold,yold=xscr,yscr

    
# testing functions connect() and circle()
for n in range(0,105,5):
  connect(3*n,200,300,200-2*n,"orange")
  connect(3*n,0,0,200-2*n,"blue")
N=20;R=50
for a in range(N):
  angle1=a/(N-1)*2*pi
  angle2=(a+N//3)/(N-1)*2*pi
  x=int(R*cos(angle1)+150+.5)
  y=int(R*sin(angle1)+100+.5)
  circle(x,y,35,"green")
N=15;R=20
for a in range(N):
  angle1=a/(N-1)*2*pi
  angle2=(a+N//3)/(N-1)*2*pi
  x=int(R*cos(angle1)+250+.5)
  y=int(R*sin(angle1)+40+.5)
  circle(x,y,10,"red")
  x=int(R*cos(angle1)+50+.5)
  y=int(R*sin(angle1)+160+.5)
  circle(x,y,10,"red")
for r in range(2,12,2):
  circle(150,100,r,"orange")
    
     
# only for running under Cpython:
kandinsky.mainloop()


