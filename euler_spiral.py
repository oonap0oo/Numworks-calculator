import kandinsky

# factorial not natively available in Numworks
def factorial(n):
  fact=1
  for k in range(2,n+1):
    fact*=k
  return fact

# Fresnel integrals using Maclaurin series 
def S(x,Nsteps):
  sum=0
  sign=1
  for n in range(Nsteps):
    sum+=sign*x**(4*n+3)/(factorial(2*n+1)*(4*n+3))
    sign=-sign
  return sum

def C(x,Nsteps):
  sum=0
  sign=1
  for n in range(Nsteps):
    sum+=sign*x**(4*n+1)/(factorial(2*n)*(4*n+1))
    sign=-sign
  return sum

# draw a line between any two points
def connect(x1,y1,x2,y2,co="black"):
  xspan=x2-x1;yspan=y2-y1
  steps=max(abs(xspan),abs(yspan))
  if steps==0:
    kandinsky.set_pixel(x1,y1,co)
    return
  dx=xspan/steps;dy=yspan/steps
  x=x1;y=y1
  for k in range(steps):
    kandinsky.set_pixel(int(x+.5),int(y+.5),co)
    x+=dx;y+=dy

kandinsky.fill_rect(0,0,320,230,"black")

# parameters
Npoints=800 # number of x,y points calculated
Nmaclaurin=50 # number of terms for series
# drawing loop
first_iter=True
for k in range(-Npoints//2,Npoints//2):
  p=10*k/(Npoints-1) # variable used for Maclaurin series
  x=int(160+C(p,Nmaclaurin)*110+.5)
  y=int(115-110*S(p,Nmaclaurin)+.5)
  if first_iter: # first run initialise x_old,y°old
    x_old,y_old=x,y
    first_iter=False
  connect(x_old,y_old,x,y,"white")
  x_old,y_old=x,y
kandinsky.draw_string("Euler's Spiral",20,20,"white","black")
    
