# mass-spring-damper
# d2x/dt2 + 2*ζ*ωn*dx/dt + ωn**2*x = 0
# v = dx/dt
#
# dv/dt + 2*ζ*ωn*v + ωn**2*x = 0
#
# dv/dt = -2*ζ*ωn*v - ωn**2*x
# dx/dt = v
#
# ωn = sqrt(k/m)
# ζ = c/(2*m*ωn)
#
#Undamped systems ζ = 0
#Underdamped systems ζ < 1
#Critically damped systems ζ = 1
#Overdamped systems ζ > 1

from math import *
import matplotlib.pyplot as plt

# Euler method applied on mass-spring-damper system
def euler_mass_spring(x,v,h,zeta,omega_n):
  d_v_dt=-2*zeta*omega_n*v-omega_n**2*x # mass-spring-damper system
  d_x_dt=v
  v_new=v+d_v_dt*h # Euler method
  x_new=x+d_x_dt*h
  return(x_new,v_new)

# system parameters
zeta=0.1 #damping ratio ζ
omega_n=2*pi*1.0 #Natural frequency ωn in rad/s
# initial conditions
x=1
v=0
# calculation parameters
T=3 #total time in s
N_plot=100 # number of points to plot
N_extra=200 # number of points to calculate between each plot point
#time step
h=T/(N_plot*N_extra)
# list to contain x values
x_arr=[0]*N_plot
# loop
for k in range(N_plot):
    x_arr[k]=x
    for _ in range(N_extra):
      x,v=euler_mass_spring(x,v,h,zeta,omega_n)
#list to contain t values
t_arr=[t/(N_plot-1)*T for t in range(N_plot)]
#plot
plt.plot(t_arr,x_arr)
plt.text(T/8,1,"Mass-Spring-Damper system")
plt.text(T/8,0.7,"Damping ζ = {0:.2f}".format(zeta))
plt.text(T/8,0.85,"Natural frequency ωn = {0:.2f} rad/s".format(omega_n))
plt.grid()
plt.show()


  
  
  

