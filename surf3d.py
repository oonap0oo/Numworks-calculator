import kandinsky
from math import *

# functions to plot
def sinc(x,y):
  r=sqrt(x**2+y**2)
  z=sin(r)/r
  return z

def sincos(x,y):
  z=sin(x)*cos(y)
  return z

#plotting function
#fun: function to plot must take 2 arguments, return 1
#xrange,yrange,zrange: tuples with (min,max) value
#txt; text which is added to the plot, optional
def surf(fun,xrange,yrange,zrange,txt=""):    
  Nx=220
  Ny=64
  # Ny*xshift + Nx = 300
  # => xshift = (300 - Nx) / Ny
  xshift=(300-Nx)/Ny
  yshift=xshift
  kandinsky.fill_rect(0,0,320,240,"black")
  for v in range(Ny,0,-1):
    y=yrange[0]+(yrange[1]-yrange[0])*v/(Ny-1)
    dx=v*xshift
    dy=v*yshift
    for h in range(Nx):
      x=xrange[0]+(xrange[1]-xrange[0])*h/(Nx-1)
      funz=fun(x,y)
      x_screen=int(h+dx+10)
      z=(funz-zrange[0])/(zrange[1]-zrange[0])*150
      y_screen=int(200-(z+dy))
      c=int((1-v/Ny)*200+z/150*200+40)
      c=max(0, min(c, 255))
      kandinsky.set_pixel(x_screen,y_screen,kandinsky.color(c,c,c))
  kandinsky.draw_string(txt,30,10,"white","black")

# function call to plot surface 
surf(sinc,(-12, 12),(-12, 12),(-0.1, 1.0),"z=sinc(x,y)")
#surf(sincos,(-4,4),(-4,4),(-1,2),"sinxcos")



