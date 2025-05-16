from kandinsky import *
for x in range(320):
  re=x/319*3.5-2.5
  for y in range(210):
    im=y/219*2.5-1.25 
    c=complex(re,im)
    z=0
    i=0
    while abs(z)<2 and i<255:
      z=z**2+c
      i+=1
    r=(i % 64)*4
    g=(i % 32)*8
    b=(i % 16)*16
    set_pixel(x,y,color(r,g,b))
