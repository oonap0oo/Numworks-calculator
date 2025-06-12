import kandinsky
from math import *
a = 2.879879# constants 
b = -0.765145
c = -0.966918
d = 0.744728

def draw_fractal(N=100000):
  x,y=2.0,2.0 # initial values
  kandinsky.fill_rect(0,0,320,230,"black")
  for _ in range(N):
      x,y=sin(a*x)+b*sin(a*y),sin(c*x)+d*sin(c*y)
      xscr=int(300*(x+2)/4+10)
      yscr=int(220*(y+2)/4+10)
      pr,pg,pb=kandinsky.get_pixel(xscr,yscr)
      pr+=30;pg+=10;pb+=50 # increase color
      pr=min(255,pr) # clip color
      pg=min(255,pg)
      pb=min(255,pb)
      kandinsky.set_pixel(xscr,yscr,(pr,pg,pb))
  kandinsky.draw_string("King's Dream Fractal",10,5,(180,127,255),"black")

draw_fractal()
