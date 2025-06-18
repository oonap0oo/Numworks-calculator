from math import *
import matplotlib.pyplot as plt
# finction to apply integration on
def sinfun(x):
  return sin(x)
# 1/3 simpson rule to calc definite integral  
def simpson(fun,a,b,n):
  h=(b-a)/n
  intg=fun(a)+fun(b)
  factor=4
  for k in range(1,n):
    x=a+(b-a)*k/n
    intg+=factor*fun(x)
    factor=4 if factor==2 else 2
  intg*=h/3
  return intg  
# calc definite integral
a=0;b=pi;n=200
intg = simpson(sinfun,a,b,n)
# preparing plot making lists for x and y
x_lst=[a+(b-a)*k/200 for k in range(1,200)]
f_lst=[sinfun(x) for x in x_lst]
plt.bar(x_lst,f_lst,0.02)
#preparing txt to add
txt="Integral from {0:.2f} to {1:.2f} = {2:.8f}".format(a,b,intg)
ytxt=min(f_lst)+(max(f_lst)-min(f_lst))*1.2
plt.text(a,ytxt,txt)
# show the plot
plt.show()
