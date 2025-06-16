from kandinsky import *
from time import *
from ion import *
# possible characters and the on-state of each segment
logic={
  "0":(True,True,True,False,True,True,True),
  "1":(False,False,True,False,False,True,False),
  "2":(True,False,True,True,True,False,True),
  "3":(True,False,True,True,False,True,True),
  "4":(False,True,True,True,False,True,False),
  "5":(True,True,False,True,False,True,True),
  "6":(True,True,False,True,True,True,True),
  "7":(True,False,True,False,False,True,False),
  "8":(True,True,True,True,True,True,True),
  "9":(True,True,True,True,False,True,True),
  " ":(False,False,False,False,False,False,False),
  "_":(False,False,False,False,False,False,True),
  "-":(False,False,False,True,False,False,False),
  "|":(False,True,False,False,True,False,False),
  "=":(False,False,False,True,False,False,True)
  }
# the position and orientation of all 7 segments
segments=(
  (0,0,1,0),
  (0,0,0,1),
  (1,0,0,1),
  (0,1,1,0),
  (0,1,0,1),
  (1,1,0,1),
  (0,2,1,0),
)
# parameters
bgcol="black"
dispcol="red"
txtcol="white"
# draw 1 7 segment character
def draw1display(char,pos,dec=False,l=15,w=5):
  xpos,ypos=pos
  gap=w
  fill_rect(xpos+10,ypos+10,l+4*w,2*l+5*w,bgcol)
  if char in logic:
    for state,segment in zip(logic[char],segments):
      if state:
        x,y,dx,dy=segment
        x=10+(l+2*gap)*x+gap*dx
        y=10+(l+2*gap)*y+gap*dy
        dx=w+dx*l;
        dy=w+dy*l
        fill_rect(x+xpos,y+ypos,dx,dy,dispcol)
  if dec:
    x=10+l+3*gap+2
    y=10+(l+2*gap)*2
    fill_rect(x+xpos,y+ypos,w,w,"red")
# draw str as 7 segment chars
def drawmultiple(txt,pos,l=15,w=5):
  dx=0
  for k in range(len(txt)):
    if txt[k]!=".":
      if k<(len(txt)-1):
        dec=txt[k+1]=="."
      x=pos[0]+dx*(l+5*w)
      y=pos[1]
      draw1display(txt[k],(x,y),dec,l,w)
      dx+=1
# diplay of stopwatch
fill_rect(0,0,320,230,bgcol)
draw_string("Stopwatch",5,10,txtcol,bgcol)
draw_string("right arrow key to start",5,30,txtcol,bgcol)
draw_string("left arrow key to stop",5,50,txtcol,bgcol)
draw_string("down arrow key to reset",5,70,txtcol,bgcol)
# main loop
running=False;first=True
total=0
formatstr="{:07.2f}" # format of time str
drawmultiple(formatstr.format(0.0),(15,100))
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
    drawmultiple(formatstr.format(0.0),(15,100))
    total=0
  if running==True:
    now=monotonic()
    t=now-start+total  
    drawmultiple(formatstr.format(t),(15,100))
