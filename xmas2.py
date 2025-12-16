# XMAS tree using turtle
from turtle import *
from math import * 
from random import *

# draws 1 star at x,y with given size
def star(x,y,size):
  penup()
  goto(x,y)
  pendown()
  for _ in range(5):
    forward(size)
    right(144)

# parameters
N=250
Nstar=20
cycles=13
col=("blue","red","yellow","pink","orange","purple")
col_bg=(20,20,100)
col_bg_star=(30,30,150)
# turtle settings
speed(0)
hideturtle()
colormode(255)
# background
color(col_bg)
pensize(120)
goto(-150,0)
goto(150,0)
goto(-150,100)
goto(150,100)
goto(-150,-80)
goto(150,-80)
# background stars
pensize(2)
color(col_bg_star)
for _ in range(25):
  star(randint(-150,150),randint(-50,100),18)
# draw trunk
color("brown")
pensize(10)
penup()
goto(0,-50)
pendown()
goto(0,-90)
# draw tree
color("green")
pensize(4)
for k in range(N):
  kn=k/(N-1)
  angle=kn*2*3.14*cycles
  x=int((90*kn+4)*cos(angle))
  y=int(100-150*kn+20*kn*sin(angle))
  if k==0:
    penup()
  elif k==1:
    pendown()
  goto(x,y)
# draw stars on tree
pensize(7)
for k in range(Nstar):
  kn=k/(Nstar)
  angle=kn*2*3.14*cycles
  x=int((100*kn+4)*cos(angle))
  y=int(100-150*kn+20*kn*sin(angle))
  color(choice(col))
  star(x,y,8)



