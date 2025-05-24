from time import *
from ion import *
from kandinsky import *

draw_string("Stopwatch",5,10)
draw_string("right arrow key to start",5,30)
draw_string("left arrow key to stop",5,50)
draw_string("down arrow key to reset",5,70)

running=False;first=True
total=0
formatstr="time: {:6.2f}s"
draw_string(formatstr.format(0.0),15,100)
while True:
  #start
  if keydown(KEY_RIGHT)==True:
    if running==False:
      if first==True:  
        first=False
      start=monotonic()
      running=True
  #stop    
  if keydown(KEY_LEFT)==True:
    if running==True:
      running=False
      total=t
  #reset
  if keydown(KEY_DOWN)==True:
    draw_string(formatstr.format(0.0),15,100)
    total=0
  if running==True:
    now=monotonic()
    t=now-start+total  
    draw_string(formatstr.format(t),15,100)
   
