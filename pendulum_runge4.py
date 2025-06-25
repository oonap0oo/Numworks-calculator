# Driven damped pendulum
# I*d(dθ/dt)/dt + m*g*l*sin(θ) + b*dθ/dt = a*cos(Ω*t)
# I = m*l**2 : moment of inertia
# each term is torque
# d(dθ/dt)/dt = 1/I*( -g*m*l*sin(θ) - b*dθ/dt + a*cos(Ω*t) )
# dθ/dt = ω
# d(dθ/dt)/dt = dω/dt
######################################################
# system of 1 order ODE:
# dω/dt = 1/I*( -g*m/l*sin(θ) - b*ω + a*cos(Ω*t) )
# dθ/dt = ω
######################################################
# m: mass at end of pendulum
# l: length pendulum
# θ: angular deflection of pendulum
# ω: angular speed of pendulum
# I: moment of inertia
# g: gravitational acceleration
# b: friction coefficient propotional to angular speed
# a: amplitude of driving torque
# Ω: angular frequency of driving force

from math import *
import matplotlib.pyplot as plt
import numpy as np

# derivative of angular velocity omega
def domega_dt(theta,omega,g,l,b,I,omega_driven,t):
  t1=-g*I/l*sin(theta) # deflection pendulum
  t2=-b*omega # damping
  t3=a*cos(omega_driven*t) # driving force
  return (t1+t2+t3)/I

# derivative of angle theta is omega
def dtheta_dt(omega):
  return omega
  
# 4-order Runge-Kutta method applied to pendulum
def runge_kutta_pendulum(omega,theta,h,g,l,b,I,omega_driven,t):
  k1=domega_dt(theta,omega,g,l,b,I,omega_driven,t)
  k2=domega_dt(theta+h*k1/2,omega+h*k1/2,g,l,b,I,omega_driven,t)
  k3=domega_dt(theta+h*k2/2,omega+h*k2/2,g,l,b,I,omega_driven,t)
  k4=domega_dt(theta+h*k3,omega+h*k3,g,l,b,I,omega_driven,t)
  omega_new=omega+h*(k1+2*k2+2*k3+k4)/6
  k1=dtheta_dt(omega)
  k2=dtheta_dt(omega+h*k1/2)
  k3=dtheta_dt(omega+h*k2/2)
  k4=dtheta_dt(omega+h*k3)
  theta_new=theta+h*(k1+2*k2+2*k3+k4)/6
  return(omega_new,theta_new)

# system parameters
# constant 
g=9.81
# parameters
l=1 #length pendulum in meter
b=0.4 #degree of damping
m=1 #mass mendulum weight in kg
omega_driven=2*pi*1 #angular frequency driving force
a=8 #amplitude driving force
# initial conditions
theta=radians(45)
omega=0
t=0
# calculation parameters
T=25 #total time in s
N_plot=200 # number of points to plot
N_extra=100 # number of points to calculate between each plot point
#time step
h=T/(N_plot*N_extra)
#moment of inertia
I=m*l**2 # calculating I once here iso. in each iteration
# list to contain x values
#theta_arr=[0]*N_plot
theta_deg_arr=np.zeros(N_plot)
#list to contain t values
#t_arr=[0]*N_plot
t_arr=np.zeros(N_plot)
print("Calculating {0} points".format(N_plot*N_extra))
# loop
for k in range(N_plot):
    theta_deg_arr[k]=degrees(theta)
    t_arr[k]=t
    for _ in range(N_extra): # extra calculations to keep h small
      omega,theta=runge_kutta_pendulum(omega,theta,h,g,l,b,I,omega_driven,t)
      t+=h
#plot
plt.plot(t_arr,theta_deg_arr)
plt.text(T/10,48,"Pendulum system, damped and driven")
plt.text(T/10,38,"Using Runge-Kutta Method")
plt.grid()
plt.show()


  
  
  

