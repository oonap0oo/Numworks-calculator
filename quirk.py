import numpy as np
#x is numpy ndarray
x=np.linspace(0,1,6)
#a is scalar, float in this case
a=3.5
#b is numpy ndarray of 1 element
b=np.array([3.0])
#runs ok
y=x*a;y2=x+a
print("scalar can be int of float")
print("ok: numpyarray * scalar")
print("ok: numpyarray + scalar")
y3=x*b;y4=b*x;y5=x+b;y6=b+x
print("ok: numpyarray * numpyarray")
print("ok: numpyarray + numpyarray")
#following operations give error
print("These operations give error")
print("on the Numworks calc:")
print("\"TypeError: Unsupported types\"")
try:
  z=a*x
except:
  print("error: scalar * numpyarray")
else:
  print("ok: scalar * numpyarray")
try:
  z2=a+x
except:
  print("error: scalar + numpyarray")
else:
  print("ok: scalar + numpyarray")
