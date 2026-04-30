from kandinsky import *
from math import *

# functions to plot
def sinc(x,y):
  r=sqrt(x**2+y**2)
  z=sin(r)/r
  return z

def sincos(x,y):
  z=sin(x)*cos(y)
  return z

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

#plotting function
#fun: function to plot must take 2 arguments, return 1
#xrange,yrange,zrange: tuples with (min,max) value
#txt; text which is added to the plot, optional
def surf(fun,xrange,yrange,zrange,txt=""):
  nh=120;nv=60;scale=120
  alpha=pi/4;k=0.4
  fmax=[0]*320;fmin=[0]*320
  xmin,xmax=xrange;ymin,ymax=yrange;zmin,zmax=zrange;
  hm=160;vm=110
  ca=k*cos(alpha);sa=k*sin(alpha)
  dy=(ymax-ymin)/nv;dx=(xmax-xmin)/nh
  fill_rect(0,0,320,240,"black")
  y=ymin
  for v in range(nv):
    x=xmin;first1=True;first2=True
    for h in range(nh):
      z=fun(x,y)
      xx=-scale+2*(x-xmin)/(xmax-xmin)*scale
      yy=-scale+2*(y-ymin)/(ymax-ymin)*scale
      zz=-scale+2*(z-zmin)/(zmax-zmin)*scale
      xscr=int(hm+xx+yy*ca);yscr=int(vm-zz/2-sa*yy)
      xscr=max(min(319,xscr),0)
      if 240-yscr>fmax[xscr]:
        if not first1:
          connect(xscr2,yscr2,xscr,yscr,"white")
        fmax[xscr]=240-yscr
        xscr2,yscr2=xscr,yscr;first1=False 
      else:
        first1=True   
      if yscr>fmin[xscr]:
        if not first2:
          connect(xscr2,yscr2,xscr,yscr,"white")
        fmin[xscr]=yscr
        xscr2,yscr2=xscr,yscr;first2=False
      else:
        first2=True
      x+=dx
    y+=dy       
  draw_string(txt,30,10,"white","black")

# function call to plot surface 
surf(sinc,(-12, 12),(-12, 12),(-0.1, 1.0),"z=sinc(x,y)")
#surf(sincos,(-4,4),(-4,4),(-1,1),"sinxcos")
