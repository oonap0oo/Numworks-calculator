import kandinsky
from random import randint,choice
from time import sleep

def connect(x1,y1,x2,y2,co="black"):
  xspan=x2-x1;yspan=y2-y1
  steps=max(abs(xspan),abs(yspan))
  if steps==0:
    kandinsky.set_pixel(x1,y1,co)
    return
  dx=xspan/steps;dy=yspan/steps
  x=x1;y=y1
  for k in range(steps):
    kandinsky.set_pixel(int(x+.5),int(y+.5),co)
    x+=dx;y+=dy

def quadrilateral():
  x=[];y=[]
  xstep=[];ystep=[]
  for k in range(4):
    x.append(randint(0,320))
    y.append(randint(0,220))
    xstep.append(randint(1,4)*choice([-1,1]))
    ystep.append(randint(1,4)*choice([-1,1]))
  return x,y,xstep,ystep

def step(x,y,dx,dy):
  for k in range(4):
    x[k]+=dx[k];y[k]+=dy[k]
    if x[k]>=320:
      dx[k]=-dx[k]
    if x[k]<=0:
      dx[k]=-dx[k]
    if y[k]>=220:
      dy[k]=-dy[k]
    if y[k]<=0:
      dy[k]=-dy[k]
  return(x,y,dx,dy)

def drawquad(x,y,co):
  for k in range(3):
    connect(x[k],y[k],x[k+1],y[k+1],co)
  connect(x[3],y[3],x[0],y[0],co)

x,y,dx,dy=quadrilateral()
x2,y2,dx2,dy2=quadrilateral()
while True:
  #print(x,y,dx,dy)
  x,y,dx,dy=step(x,y,dx,dy)
  x2,y2,dx2,dy2=step(x2,y2,dx2,dy2)
  kandinsky.fill_rect(0,0,320,230,"black")
  drawquad(x,y,"green")
  drawquad(x2,y2,"blue")
  sleep(0.1)
