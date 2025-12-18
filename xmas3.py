# XMAS tree using kandinsky
from math import * 
from random import *
import kandinsky
import time

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

# draws 1 star at x,y with given size
def star(x,y,size,col):
  N=8
  for k in range(N):
    angle=k/(N-1)*2*pi
    x2=x+size*cos(angle)
    y2=y+size*sin(angle)
    connect(x,y,x2,y2,col)

def calcxy(angle):
  x=160+int((90*kn+4)*cos(angle))
  y=20+int(180*kn+20*kn*sin(angle))
  return x,y 

    
# parameters
N=350
Nstar=25
cycles=16
col=("red","yellow","pink","orange","purple")
col_bg=(20,20,100)
col_bg_star=(40,40,200)
# background
kandinsky.fill_rect(0,0,320,240,kandinsky.color(col_bg))
# background stars
for _ in range(40):
  star(randint(0,320),randint(0,200),9,kandinsky.color(col_bg_star))
# draw trunk
kandinsky.fill_rect(155,200,10,40,kandinsky.color("brown"))
# draw tree
for k in range(N):
  kn=k/(N-1)
  angle=kn*2*3.14*cycles
  x,y=calcxy(angle)
  if k>1:
    connect(x,y,x_old,y_old,kandinsky.color("green"))
    connect(x,y+1,x_old,y_old+1,kandinsky.color("green"))
#    connect(x,y-1,x_old,y_old-1,kandinsky.color("green"))
  x_old=x;y_old=y
while True:
  # draw stars on tree
  for k in range(Nstar):
    kn=k/(Nstar)
    angle=kn*2*3.14*cycles
    x,y=calcxy(angle)
    co = kandinsky.color(choice(col))
    star(x,y,7,co)
    star(x,y+1,7,co)
  time.sleep(0.4)



