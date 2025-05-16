from kandinsky import *
c=complex(-0.5125,0.5213)
for x in range(320):
  re=(x-160)/160*1.5
  for y in range(210):
    im=(y-105)/105
    z=complex(re,im)
    i=256
    while abs(z)<2 and i>0:
      z=z**2+c
      i-=1
    set_pixel(x,y,color(i,i,i))
