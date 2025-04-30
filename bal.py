from math import *
from matplotlib.pyplot import *
import numpy as np
def bal(t,alpha,vo):
  x=t*vo*np.cos(alpha)
  y=t*vo*np.sin(alpha)-(t**2)*0.5*9.81
  return x,y  
tt=np.linspace(0,2.5,20)
for i in (15,30,45,60,85):
  a=radians(i)
  xx,yy=bal(tt,a,10)
  plot(xx,yy)
grid()
axis((-1,15,-4,7))
show()
