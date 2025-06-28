from math import *
from cmath import phase

def out(x,s):
  print("{0}={1:.8}{2:+.8}j".format(s,x.real,x.imag))
  print("|{0}|={1:.10} Ohm".format(s,abs(x)))
  print("phase={0:.6} deg".format(degrees(phase(x))))

def zcap(c,f):
  zc=1/(2*pi*f*1j*c)
  return zc
  
def zseries(r,c,f):
  zc=zcap(c,f)
  zser=r+zc
  return zser
  
def zparall(r,c,f):
  zc=zcap(c,f)
  zp=1/(1/r+1/zc)
  return zp

def z_all():
  print("Impedance combinations of\nresistor - capacitor")
  r=float(input("r [Ohm]? "))
  c=float(input("c [Farad]? "))
  f=float(input("f [Hz]? "))  
  zc=zcap(c,f)
  zs=zseries(r,c,f)
  out(zs,"zser")
  zp=zparall(r,c,f)
  out(zp,"zpar")

z_all()

