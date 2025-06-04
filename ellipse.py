from math import *
import matplotlib.pyplot as plt

# Binomial coefficient
def binomial(n,k):
  return factorial(n)/factorial(k)/factorial(n-k)

# circumference approx. by series
def circumference(a,b,nterms=6):
  h=(a-b)**2/(a+b)**2
  series=0
  for n in range(nterms):
    bin=binomial(2*n,n)
    denom=(2*n-1)*4**n
    series+=(bin/denom)**2 * h**n
  return pi*(a+b)*series

# surface area
def area(a,b):
  return pi*a*b

# plot using matplotlib
def plot_ellipse(a,b,cir,area):
  N=100
  x=[0.0]*N;y=[0.0]*N
  for k in range(100):
    angle=2*pi*k/99
    x[k]=a*cos(angle)
    y[k]=b*sin(angle)
  w=1.4*a
  plt.axis((-w,w,w*1.1,-w*0.9))
  plt.plot(x,y)
  plt.grid()
  plt.text(-a,w*1.1,"Ellipse a={0} b={1}".format(a,b))
  plt.text(-a,w*0.9,"Circ. = {0:f} Area = {1:f}".format(cir,area))
  plt.show()

def main():
  print("Circumference of ellipse")
  a=float(input("Height of ellipse? "))/2
  b=float(input("Width of ellipse? "))/2
  cir=circumference(a,b)
  s=area(a,b)
  print("Circumference={0:f}".format(cir))
  print("Area={0:f}".format(s))
  input("Hit <Exe> for plot")
  plot_ellipse(a,b,cir,s)

main()
