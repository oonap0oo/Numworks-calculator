import random
from matplotlib.pyplot import *
import numpy as np
# output voltage of a voltage divider
def volt_div(r1,r2,v):
  return v*r2/(r1+r2)
# function optionally accepts arguments
def montecarlo(r1_n=None,r2_n=None,tol=None,Vin=None):
    N=1000 # number of data points
    if Vin==None:
        print("Monte Carlo - spread of voltage divider")
        Vin = float(input("What is the input voltage? "))
        r1_n = float(input("Value of upper resistor? "))
        r2_n = float(input("Value of lower resistor? "))
        tol = float(input("Tolerance of resistors in %? "))
    random.seed()
    Vout=np.zeros(N)
    for i in range(N):
      r1=random.uniform(r1_n*(1-tol/100),r1_n*(1+tol/100))
      r2=random.uniform(r2_n*(1-tol/100),r2_n*(1+tol/100))
      Vout[i]=volt_div(r1,r2,Vin)
    print("Calculated {} data points".format(N))
    print("mean of Vout {:.4f} V".format(np.mean(Vout)))
    print("max, min values of Vout\n","{:.4f} V".format(np.min(Vout)), "{:.4f} V".format(np.max(Vout)))
    print("std dev of Vout {:.2e} V".format(np.std(Vout)))
    input("Hit any Exe for histogram")
    hist(Vout,N//15)
    grid()
    show() 
montecarlo()
