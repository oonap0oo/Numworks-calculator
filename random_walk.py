# Two-dimensional Lattice random walk
import turtle as tl
from random import *

#parameters
step=15 # length of one step
maxx=150;maxy=100 #limits of walk
c=("red","blue","green","purple")

# settings for turle
def init_ẗurtle(): 
  tl.reset()
  tl.speed(0)
  tl.pensize(4)

init_ẗurtle() # first time intialise turtle

for k in range(8000):
  h=randint(0,3) #random heading as number from 0..3
  tl.color(c[h]) # color determined by heading
  tl.setheading(h*90) # set turtle heading in degrees
  tl.forward(step) # one step in chozen heading
  x,y=tl.position() # get current position
  if abs(x)>maxx or abs(y)>maxy: #reset if too far
    init_ẗurtle() # initializse turle again
    
