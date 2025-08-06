# Leibniz formula for pi
#
# pi ≈ 4 *  sum[ (-1)**k / (2*k + 1) ]
# for k=0 .. inf
#
import math
import numpy
import matplotlib.pyplot as plt
n_iterations=100
print("Leibniz formula for pi")
sign=1; x=0; index=0
pi_approx=numpy.zeros(n_iterations)
# optimize the formula by
# using stepped denom variable
# i.s.o. (2*k + 1)
# and sign variable i.s.o. (-1)**k
for denom in range(1,n_iterations * 2,2):
  x+=sign/denom
  sign=-sign
  pi_approx[index]=4*x
  index+=1
print("Number of iterations: {0}".format(n_iterations))
print("Approximation for pi:\n{0}".format(pi_approx[-1]))
print("Value for pi from\nmath module: {0}".format(math.pi))
print("Deviation: {0:.2} %".format(100*(pi_approx[-1]-math.pi)/math.pi))
# plot value after each iteration
plt.axis((-10,n_iterations,2.8,3.5))
plt.plot(pi_approx)
plt.plot([0,n_iterations],[math.pi,math.pi])
plt.grid()
plt.text(5, 3.5, "Leibniz formula for approx. of pi")
plt.text(5, 3.45, "Number of iterations: {0}".format(n_iterations))
plt.show()
