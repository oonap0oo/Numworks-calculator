import kandinsky
from math import *

kandinsky.fill_rect(0,0,320,230,"black")
for v in range(0,60):
  y=v/59*2-1
  for h in range(0,250):
    x=h/249*2-1
    r=sqrt(x**2+y**2)
    if r<1:
      z=sin(1.5*pi*r)+sin(3*1.5*pi*r)*0.4
      y_scr=int(y*60-z*50+110)
      x_scr=v+h+5
      c=int(255-v*3)
      kandinsky.fill_rect(x_scr,y_scr,1,150,"black")
      kandinsky.set_pixel(x_scr,y_scr,kandinsky.color(c,c,c))
kandinsky.draw_string("Fedora",10,10,"white","black")
