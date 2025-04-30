from math import *
import numpy as np
import kandinsky
# bifurcation diagram 
# of logistic map
def logistic_map(astart=3.5,aend=4):
  aspan=aend-astart
  for x in range(320):
    a=astart+aspan*x/319
    l=0.5
    y=np.zeros(240)
    for i in range(1500):
      l=a*l*(1-l)
      y[int(l*239)]+=1
    for r in range(240):
      v=y[239-r]*4
      co=kandinsky.color(v,v,v)
      kandinsky.set_pixel(x,r,co)
