import numpy as np
import matplotlib.pyplot as plt

# returns dy/dt of 
# exponential decay
def dy_dt(y,a):
  return(-a*y)

# 4-order Runge-Kutta method    
def runge_kutta(yn, h, parameter):
  k1=dy_dt(yn,parameter)
  k2=dy_dt(yn+h*k1/2,parameter)
  k3=dy_dt(yn+h*k2/2,parameter)
  k4=dy_dt(yn+h*k3,parameter)
  yn_plus_1=yn+h*(k1+2*k2+2*k3+k4)/6
  return(yn_plus_1)

# direct calculation as check
def expo_decay(t,a,yini):
  return(np.exp(-t*a)*yini)

T=5.0 #time interval
yini=1.0 #initial value
N=200 #number of steps
h=T/N #time step
a=1.0 #time constant

t_array=np.linspace(0,T,N)
y_array=np.zeros(N)
y_array[0]=yini
for k in range(1,N):
  y_array[k]=runge_kutta(y_array[k-1],h,a)

plt.plot(t_array,y_array)
plt.plot(t_array,expo_decay(t_array,a,yini))
plt.text(0.5,0.9,"runge kutta vs direct calculation")
plt.text(0.5,0.8,"of exponential decay function")
plt.grid()
plt.show()
