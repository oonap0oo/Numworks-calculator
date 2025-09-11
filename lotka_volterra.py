import numpy as np
import matplotlib.pyplot as plt

# This code calculates some solutions to an
# example Lotka–Volterra predator–prey model
#
# Lotka–Volterra predator–prey model
# ----------------------------------
#
# dx/dt = alpha.x - beta.x.y   
#
# dy/dt = -gamma*y + delta.x.y 
#
# x is the prey population
# y is the predator population density
# alpha is the maximum prey per capita
#   growth rate
# beta is the effect of the presence
#   of predators on the prey death rate
# gamma is the predator's per capita
#   death rate
# delta is the effect of the presence
#   of prey on the predator's growth rate

# Euler method applied
# on Lotka Volterra system
# returns next values for
# x and y based on prev. ones
def euler_lotka(x,y,h):
  dx_dt=alpha*x - beta*x*y # 2 ODEs for Lotka Volterra
  dy_dt=-gamma*y + delta*x*y
  x_new=x+dx_dt*h# Euler method
  y_new=y+dy_dt*h
  return(x_new,y_new)

# loop N times calc. x and y values 
# save some values in numpy arrays
# N: total number of values calc.
# Nsave: number of values for arrays
# T: total time interval
def calc_lotka(N,Nsave,T):
  h=T/N
  x_arr=np.zeros(Nsave)
  y_arr=np.zeros(Nsave)
  #initial cond.
  x=6.0; y=2.0
  Nskip=N//Nsave
  for k in range(Nsave):
    x_arr[k]=x
    y_arr[k]=y
    for _ in range(Nskip):
      x,y=euler_lotka(x,y,h)
  return x_arr,y_arr

#parameters Lotka–Volterra eq.
alpha = 2
beta = 1
gamma = 2
delta = 0.95

# parameters script
N=30000
Nsave=200
T=8

print("Lotka–Volterra\nPredator–prey model")
print("Calculating {0} values\nSaving {1} points for plot".format(N,Nsave))
print("Time interval: {0} s".format(T))

# calc x and y values
x,y=calc_lotka(N,Nsave,T)

# plot x and y result
t=np.linspace(0,T,Nsave)
plt.plot(t,x,color="blue")
plt.plot(t,y,color="red")
plt.text(0.1,7.7,"Lotka Volterra predator prey model")
plt.text(0.1,7,"blue:prey, red:predator versus time")
plt.grid(True)
plt.show()



