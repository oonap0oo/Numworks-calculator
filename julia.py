# Julia Fractal using only math
# and kandinsky libraries
from kandinsky import *
from math import *
# complex constant for julia fractal
c=complex(-0.5125,0.5213)
# calculation and plotting
for x in range(320):
  re=(x-160)/160*1.5
  for y in range(210):
    im=(y-105)/105
    z=complex(re,im)
    i=0
    while abs(z)<2 and i<1024:
      z=z**2+c
      i+=1
    # apply non linear scaling on i
    i = int(sqrt(i)*8) 
    # calculate color comp. from i
    r = i % 33 * 8; r = min(255, r) 
    g = i % 129 * 2; g = min(255, g)
    b = i % 65 * 4; b = min(255, b)
    set_pixel(x,y,color(r,g,b))

