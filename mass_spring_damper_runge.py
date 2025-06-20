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

# derivative of velocity v
def dv_dt(x,v,zeta,omega_n):
  return -2*zeta*omega_n*v-omega_n**2*x 

# derivative of position x
def dx_dt(v,zeta,omega_n):
  return v 
  
# 4-order Runge-Kutta method applied to mass-spring-damper
def runge_kutta_mass_spring(x,v,h,zeta,omega_n):
  k1=dv_dt(x,v,zeta,omega_n)
  k2=dv_dt(x+h*k1/2,v+h*k1/2,zeta,omega_n)
  k3=dv_dt(x+h*k2/2,v+h*k2/2,zeta,omega_n)
  k4=dv_dt(x+h*k3,v+h*k3,zeta,omega_n)
  v_new=v+h*(k1+2*k2+2*k3+k4)/6
  k1=dx_dt(v,zeta,omega_n)
  k2=dx_dt(v+h*k1/2,zeta,omega_n)
  k3=dx_dt(v+h*k2/2,zeta,omega_n)
  k4=dx_dt(v+h*k3,zeta,omega_n)
  x_new=x+h*(k1+2*k2+2*k3+k4)/6
  return(x_new,v_new)

# system parameters
zeta=0.1 #damping ratio ζ
omega_n=2*pi*1.0 #Natural frequency ωn in rad/s
# initial conditions
x=1
v=0
t=0
# calculation parameters
T=3 #total time in s
N_plot=100 # number of points to plot
N_extra=40 # number of points to calculate between each plot point
#time step
h=T/(N_plot*N_extra)
# list to contain x values
x_arr=[0]*N_plot
#list to contain t values
t_arr=[0]*N_plot
# loop
for k in range(N_plot):
    x_arr[k]=x
    t_arr[k]=t
    for _ in range(N_extra): # extra calculations to keep h small
      x,v=runge_kutta_mass_spring(x,v,h,zeta,omega_n)
      t+=h
#plot
plt.plot(t_arr,x_arr)
plt.text(T/8,1.05,"Mass-Spring-Damper system")
plt.text(T/8,0.95,"Using Runge-Kutta Method")
plt.text(T/8,0.75,"Damping ζ = {0:.2f}".format(zeta))
plt.text(T/8,0.85,"Natural frequency ωn = {0:.2f} rad/s".format(omega_n))
plt.grid()
plt.show()


  
  
  

