from math import *
import kandinsky
# ρ:rho
# σ : sigma
# β : Beta
#
# Lorenz System
#
# dx
#---- = σ(y - x)
# dt
#
# dy
#---- = x(ρ - z) - y
# dt
#
# dz
#---- = xy - βz
# dt

# Euler method applied on Lorenz su-ystem
def euler_lorenz(x,y,z,h,sigma,beta,rho):
  dx_dt=sigma*(y-x)# lorenz system
  dy_dt=x*(rho-z)-y
  dz_dt=x*y-beta*z
  x_new=x+dx_dt*h# Euler methos
  y_new=y+dy_dt*h
  z_new=z+dz_dt*h
  return(x_new,y_new,z_new)

# function draws a line using kandinsky library
# start point:(x1,y1), end point:(x2,y2), optional color
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

# normalization of variable within range given by tuple
def norm(v,vrange):
  v=(v-vrange[0])/(vrange[1]-vrange[0])
  return v

def draw_lorenz(N=8000,h=0.005): # N: number of steps, #h: time step
  sigma=10 #parameters Lorenz
  beta=8/3
  rho=28
  x=1.0; y=1.0; z=0.0 #initial cond.
  xrange=(-25,25)
  yrange=(-25,25)
  zrange=(-5,55)
  kandinsky.fill_rect(0,0,320,240,"black")
  for k in range(N):
    x,y,z=euler_lorenz(x,y,z,h,sigma,beta,rho)
    xnorm=norm(x,xrange)
    ynorm=norm(y,yrange)
    znorm=norm(z,zrange)
    xscr=int(20+300*xnorm)
    yscr=int(230-230*znorm)
    c=int(ynorm*255)
    c=max(0,min(255,c))
    if k==0:
        xscr_old,yscr_old=xscr,yscr
    connect(xscr_old,yscr_old,xscr,yscr,kandinsky.color(255-c,0,c))
    xscr_old,yscr_old=xscr,yscr
    kandinsky.draw_string("Lorenz",20,5,"blue","black")
  
draw_lorenz()

