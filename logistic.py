from math import *
import numpy as np
import kandinsky
# bifurcation diagram 
# of logistic map
def logistic_map(astart=3.5,aend=4):
  aspan=aend-astart
  stap=4
  for x in range(320):
    a=astart+aspan*x/319
    l=0.5
    y=np.zeros(240)
    for i in range(1500):
      l=a*l*(1-l)
      y[int(l*239)]+=stap  
    for r in range(240):
      if y[239-r]>255:
        y[239-r]=255
      co=kandinsky.color(y[239-r],y[239-r],y[239-r])
      kandinsky.set_pixel(x,r,co)

logistic_map()
