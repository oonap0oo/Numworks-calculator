# Determine machine epsilon through test
#
# epsilon is smallest value such that (1.0 + epsilon) is still distinguishable from 1.0
# by the system

eps=1.0
x=1.0
exponent=0
while True: # loop until half_eps is too small to change value of x
  half_eps = eps / 2.0
  if x == x + half_eps:
    break
  eps = half_eps
  exponent-=1
print("Determine machine epsilon\nthrough test")
print("\nepsilon = {0}\n= 2**({1:.0f})".format(eps,exponent))
print("1.0 + eps = {0:.20f}".format(x+eps))
print("1.0 + eps/2 = {0:.20f}".format(x+half_eps))

