# Durand–Kerner for quadratic equations
# f(x) = x**4 + a * x**3 + b * x**2 + c * x + d = 0

# returns value of polynomial for x
# f(x) = x**4 + a * x**3 + b * x**2 + c * x + d
def poly_value(coeff, x):
  a, b, c, d = coeff
  return x**4 + a * x**3 + b * x**2 + c * x + d

# calculates next interation for Durand–Kerner method
# returns new values for roots p, q, r, s
def durand_kerner_iteration(roots):
  p, q, r, s = roots
  p_new = p - poly_value(coeff,p) / ( (p - q)*(p - r)*(p - s) )
  q_new = q - poly_value(coeff,q) / ( (q - p_new)*(q - r)*(q - s) )
  r_new = r - poly_value(coeff,r) / ( (r - p_new)*(r - q_new)*(r - s) )
  s_new = s - poly_value(coeff,s) / ( (s - p_new)*(s - q_new)*(s - r_new) )
  return [p_new, q_new, r_new, s_new]

# returns string containing rectangular representation of complex number
def c_format_rect(z):
  if z == 0.0:
    expr = "0.0"
  elif abs(z.real) > abs(z.imag * 1e12):
    expr = "{0:.8}".format(z.real)
  else:
    expr = "{0:.8}{1:+.8}*j".format(z.real,z.imag)
  return expr

# function returns True if the string is a valid float number
def isfloat(x_str):
  try:
    float(x_str)
  except:
    valid = False
  else:
    valid = True
  finally:
    return valid
  
# function retrieves number from user
# repeats input if not valid float
def input_number(prompt):
  valid = False
  while valid == False:
    answer = input(prompt)
    valid = isfloat(answer)
    if valid == True:
      return float(answer)
    print("{0} not a valid float".format(answer))

# returns biggest delta between new and old sets of root values
def roots_delta(roots_new, roots_old):
  max_delta = 0
  for old, new in zip(roots_new, roots_old):
    max_delta = max(max_delta, abs(new-old))
  return max_delta

# ******* parameters script ********
# when the roots change less then this value, iterations are stopped
max_delta_roots = 1e-10
# maximum number of iteratons allowed
max_loops = 100 

# initial values roots
# roots = [p, q, r, s]
base_value = 0.4+0.9j
roots = [base_value**k for k in range(4)]

# input coefficients of equation
print("Quadratic equation")
print("Durand Kerner method")
print("x**4+a*x**3+b*x**2+c*x+d=0")
coeff = []
for coeff_name in ("a","b","c","d"):
  value = input_number("input {0} = ".format(coeff_name))
  coeff.append(value)

# loop Durand–Kerner
roots_old = roots
for loop in range(max_loops):
  roots = durand_kerner_iteration(roots_old)
  if roots_delta(roots, roots_old) < max_delta_roots:
    break
  roots_old = roots

# feedback about number of iterations
if loop == (max_loops - 1):
  print("maximum number of iterations\ndone without reaching conversion")
else:
  print("{0} iterations done\nconversion reached".format(loop))

# results
count=("second","third","fourth")
print("Roots:")
for n, root in enumerate(roots):
  print("x{0}={1}".format(n+1,c_format_rect(root)))
  print("abs(Residual)\n={0:.8}".format(abs(poly_value(coeff, root))))
  if n<len(roots)-1:
    input("..Hit Exe for {0} root".format(count[n]))
print("...Script finished\nresults available in <list> roots")


    
