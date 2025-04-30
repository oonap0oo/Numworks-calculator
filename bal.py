from math import *
from matplotlib.pyplot import *
import numpy as np
def bal(t,alpha,vo):
  x=t*vo*np.cos(alpha)
  y=t*vo*np.sin(alpha)-(t**2)*0.5*9.81
  return x,y
def drawcurves():
  tt=np.linspace(0,2.5,20)
  angles=np.linspace(5,85,8)
  for i in angles:
    a=radians(i)
    xx,yy=bal(tt,a,10)
    plot(xx,yy)
  grid()
  axis((-1,13,-2,6))
  show()

drawcurves()
