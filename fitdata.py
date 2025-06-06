import numpy as np
import matplotlib.pyplot as plt

# data points
data_x=(2,4,8,12,15,18,21,23,27,29)
data_y=(-16.1,-3.8,8.9,1.8,-3.5,-6.2,2.4,12.2,26.3,42.2)

# sting repr. of polynomial
def pol2str(pol):
  s=""
  for k,coeff in enumerate(pol):
    p=(len(pol)-1)-k
    if p==0:
      s+="{0:+f}".format(coeff)
    elif p==1:
      s+="{0:+f}*X".format(coeff)
    else:
      s+="{0:+f}*X**{1}\n".format(coeff,p)
  return s
# plot data
plt.scatter(data_x,data_y,color="blue")
# calc and plot polynomials
colors=("red","green","orange","purple")
x=np.linspace(data_x[0],data_x[-1],20)
for d in range(1,4):
  pol=np.polyfit(data_x,data_y,d)
  print("Fit polynomial of degree {0}".format(d))
  print(pol2str(pol)) 
  fit_y=np.polyval(pol,x)
  plt.plot(x,fit_y,color=colors[d-1])
plt.grid()
input("Hit <Exe> for graph")
plt.show()
