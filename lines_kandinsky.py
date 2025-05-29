import kandinsky
from math import *

# function draws a line using kandinsky library
# start point:(x1,y1), end point:(x2,y2)
# optionally color can be specified
def connect(x1,y1,x2,y2,co="black"):
  xspan=x2-x1;yspan=y2-y1
  steps=max(abs(xspan),abs(yspan))
  dx=xspan/steps;dy=yspan/steps
  x=x1;y=y1
  for k in range(steps):
    kandinsky.set_pixel(int(x+.5),int(y+.5),co)
    x+=dx;y+=dy
    
# testing function connect()
for n in range(0,105,5):
  connect(3*n,200,300,200-2*n,"red")
  connect(3*n,0,0,200-2*n,"green")
N=40;R=100
for a in range(N):
  angle1=a/(N-1)*2*pi
  angle2=(a+N//3)/(N-1)*2*pi
  x1=int(R*cos(angle1)+150+.5)
  y1=int(R*sin(angle1)+100+.5)
  x2=int(R*cos(angle2)+150+.5)
  y2=int(R*sin(angle2)+100+.5)
  connect(x1,y1,x2,y2,"blue")
    



