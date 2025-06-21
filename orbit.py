from math import *
import kandinsky
import time
import ion

#constants
G=6.6743015e-11 #m3/(kg.s2)
m_earth=5.97219e24 #kg
h_geostat=35786e3 #m
r_earth=6378e3 #m
v_geostat=3.07e3 #m/s
# parameter
scale=6e5 #size of the image

# acceleration due to gravity
def accel(x,y):
  r=sqrt(x**2+y**2) #distance
  a=-G*m_earth/r**2 #total acceleration
  ax=a*x/r # x and y components
  ay=a*y/r
  return ax,ay

# calculate and draw 1 trajectory
def draw_traject(x,y,vx,vy,T,N,col):
  dt=T/N
  for k in range(N):
    x_scr=int(160.5+x/scale)
    y_scr=int(115.5-y/scale)
    kandinsky.set_pixel(x_scr,y_scr,col)
    ax,ay=accel(x,y)
    vx+=ax*dt; vy+=ay*dt
    x+=vx*dt; y+=vy*dt
    if k%50==0:
      kandinsky.draw_string("x={0:.1f} km y={1:.1f} km  ".format(x/1e3,y/1e3),10,5,"white","black")
      time.sleep(.08)
      if ion.keydown(ion.KEY_EXE):
        return True
  return False

# show 2 trajectories
# parameters
N_points=2000 
T_total=9e4 #s
# loop
stop=False
while not stop:
  kandinsky.fill_rect(0,0,320,230,"black")
  kandinsky.fill_rect(158,113,4,4,"blue")
  kandinsky.draw_string("EXE to stop",10,200,"white","black")
  # trajectory 1
  kandinsky.draw_string("Geostationary orbit",60,25,"green","black")
  stop=draw_traject(r_earth+h_geostat,0,0,v_geostat,T_total,N_points,"green")
  # trajectory 2
  kandinsky.draw_string("Elliptical orbit",120,190,"red","black")
  stop=draw_traject((r_earth+h_geostat)*1.8,0,0,v_geostat*0.3,T_total,N_points,"red")


  


