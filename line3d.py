import kandinsky
from math import *

# functions to plot
def spiral(t):
  x=t*cos(3*t); y=t*sin(3*t); z=sqrt(t)
  return x,y,z

def sphere(t):
  x=sqrt(100-t**2)*sin(5*t); y=sqrt(100-t**2)*cos(5*t); z=t
  return x,y,z

def wave(t):
  x=sin(6*t)*exp(-t**2/20); y=cos(6*t)*exp(-t**2/20); z=t
  return x,y,z

# function draws a line using kandinsky library
# start point:(x1,y1), end point:(x2,y2), optional color
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

# simple projection 3d to 2d
def proj(x,y,z,a,b):
  xproj=x-a*y
  yproj=z-b*y
  return xproj,yproj

# normalization of variable within range given by tuple
def norm(v,vrange):
  v=(v-vrange[0])/(vrange[1]-vrange[0])
  return v

#plotting function
#fun: function to plot must take 1 argument, return 3
#xrange,yrange,zrange: tuples with (min,max) value
#txt; text which is added to the plot, optional
def line(fun,trange,xrange,yrange,zrange,txt=""):
  kandinsky.fill_rect(0,0,320,240,"black")
  hoek=pi/12
  a=cos(hoek);b=sin(hoek)
  Nt=3000
  for k in range(Nt):
    t=trange[0]+(k/(Nt-1)*(trange[1]-trange[0]))
    x,y,z=fun(t)
    x=norm(x,xrange)
    y=norm(y,yrange)
    z=norm(z,zrange)
    xproj,yproj=proj(x,y,z,a,b)
    xproj=norm(xproj,(-a,1))
    yproj=norm(yproj,(-b,1))
    xscr=int(20+300*xproj)
    yscr=int(230-230*yproj)
    c=int(y*220+60)
    c=max(0,min(255,c))
    if k==0:
        xscr_old,yscr_old=xscr,yscr
    connect(xscr_old,yscr_old,xscr,yscr,kandinsky.color(c,c,c))
    xscr_old,yscr_old=xscr,yscr
  kandinsky.draw_string(txt,30,10,"white","black")
    
# calling the plotting function

#line(spiral,(0,pi*12),(-37,37),(-37,37),(0,6.5),"spiral")
#line(sphere,(-10,10),(-10,10),(-10,10),(-10,10),"sphere")
line(wave,(-10,10),(-1,1),(-1,1),(-10,10),"wave")

    



