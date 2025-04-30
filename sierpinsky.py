from math import *
import kandinsky
import random
def sierp(n=50000):
  cs=('red','blue','green')
  h=((160,10),(10,210),(310,210))
  px=100;py=100;oldk=0
  for i in range(n):
    k=random.randint(0,2)
    px=0.5*(px+h[k][0])
    py=0.5*(py+h[k][1])
    kandinsky.set_pixel(int(px),int(py),cs[oldk])
    oldk=k
