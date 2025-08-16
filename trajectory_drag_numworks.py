# ballistic trajectory of projectile
# with drag proportional to square
# of velocity
#
#  v = sqrt(vx**2 + vy**2)
#  dx/dt = vx
#  dy/dt = vy
#  dvx/dt = -mu * vx * v
#  dvy/dt = -g - mu * vy * v

from math import *
import matplotlib.pyplot as plt

# functions applies Euler's method
# on system of 1 order ODEs
def euler():
  x_arr = []
  y_arr = []
  # init conditions
  x = x0
  y = y0
  vx = vx0
  vy = vy0
  # euler time step
  h = T / N
  nsave = N // Nsave
  for k in range(N):
    if k % nsave == 0:
      x_arr.append(x)
      y_arr.append(y)
    # total velocity
    v = sqrt(vx**2 + vy**2)
    # system of ODEs for trajectory
    # with Newton drag
    dx_dt = vx
    dy_dt = vy
    dvx_dt = -mu * vx * v
    dvy_dt = -g - mu * vy * v
    # calc new values out of derivatives
    x += h * dx_dt
    y += h * dy_dt
    vx += h * dvx_dt
    vy += h * dvy_dt
    # stop if projectile hits ground
    if y < 0:
      break
  return (x_arr, y_arr)

# parameters
mu = 0.01 # factor related to drag
g = 9.81 # acceleration gravity
N = 5000 # number of steps
Nsave = 200 # number steps saved
T = 10 # total time interval calculated
# intial conditions
x0 = 0; y0 = 0
vx0 = 100
vy0 = 100

# perform euler calc
x_arr, y_arr = euler()
# show some stats
print("number of points",len(x_arr))
print("ymax=",max(y_arr))
print("xmax=",max(x_arr))
# plot
plt.plot(x_arr,y_arr)
plt.grid(True)
plt.show()
