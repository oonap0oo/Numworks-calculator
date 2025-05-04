from math import *
import kandinsky
import time

def ellipse(xc, yc, w, h, N, angle):
  for i in range(N):
      x = w * sin(2 * pi* i / N)
      y = h * cos(2 * pi * i / N)
      xr = cos(angle) * x - sin(angle) * y
      yr = sin(angle) * x + cos(angle) * y
      xr += xc
      yr += yc
      kandinsky.set_pixel(int(xr), int(yr), "yellow")
for turns in range(2):
    angle_steps = 40
    np=100
    for a in range(angle_steps):
      angle = 2 * pi * a / angle_steps
      kandinsky.fill_rect(0,0,320,240,"black")
      for k in range(0, 120, 20):
        ellipse(160, 110, k, 100, np, angle)
      for k in range(0, 120, 20):
        ellipse(160, 110, 100, k, np, angle)      
      time.sleep(0.2)
