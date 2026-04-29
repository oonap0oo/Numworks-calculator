# Sphere with hidden-line removal.  K Moerman 2026
from math import *
from kandinsky import *

# function draws a line using kandinsky library
# start point:(x1,y1), end point:(x2,y2), optional color
def connect(x1,y1,x2,y2,co="black"):
  xspan=x2-x1;yspan=y2-y1
  steps=max(abs(xspan),abs(yspan))
  if steps==0:
    set_pixel(x1,y1,co)
    return
  dx=xspan/steps;dy=yspan/steps
  x=x1;y=y1
  for k in range(steps):
    set_pixel(int(x+.5),int(y+.5),co)
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

n1=15 # number of latitude lines
n2=40 # number of longitude lines
r=100 # radius of sphere
rot=-pi/4 # rotation angle around x axis
co=color(0,255,0);bgco=color(0,0,0) # line color
# draw background and circumference
fill_rect(0,0,320,240,bgco)
circle(160,110,r,co)
# calc. some values
rcos=cos(rot);rsin=sin(rot)
da1=pi/(n1-1);da2=2*pi/(n2-1)
# main drawing loop
xp=[0]*n1;yp=[0]*n1;a2=0
for i in range(n2):
  fk=True;a1=0
  for k in range(n1):
    x=r*sin(a1)*cos(a2) # spherical to cartesian
    y=r*sin(a1)*sin(a2) # coordinates
    z=r*cos(a1)
    zr=rcos*z-rsin*y # rotate sphere
    yr=rsin*z+rcos*y
    xscr=int(160+x);yscr=int(110+zr)
    if yr>=-1: # if line should be visible    
      if not fk:
        connect(xscr,yscr,xscr2,yscr2,co)
        if i>0:
          connect(xscr,yscr,xp[k],yp[k],co)       
      xscr2=xscr;yscr2=yscr;fk=False
    xp[k]=xscr;yp[k]=yscr
    a1=a1+da1
  a2=a2+da2


