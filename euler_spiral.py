import kandinsky

# Fresnel integrals using Maclaurin series 
def fresnel(x, Nsteps):
    S = 0; C = 0
    sign = 1  
    for n in range(Nsteps):
        fact_2n = fact_2n_plus_1 * 2 * n if n > 0 else 1 # 0! = 1
        fact_2n_plus_1 = fact_2n * (2*n + 1) # (2n+1)! = (2n+1).(2n)!
        S += sign * x**(4*n + 3) / ( fact_2n_plus_1 * (4*n + 3) )
        C += sign * x**(4*n + 1) / ( fact_2n * (4*n + 1) )
        sign = -sign
    return S, C

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

# parameters
Npoints=800 # number of x,y points calculated
Nmaclaurin=50 # number of terms for series
# drawing loop
kandinsky.fill_rect(0,0,320,230,"black")
first_iter=True
for k in range(-Npoints//2,Npoints//2):
  p=10*k/(Npoints-1) # variable used for Maclaurin series
  S_fresnel, C_fresnel = fresnel(p, Nmaclaurin)
  x=int(160+C_fresnel*110+.5)
  y=int(115-110*S_fresnel+.5)
  if first_iter: # first run initialise x_old,y°old
    x_old,y_old=x,y
    first_iter=False
  connect(x_old,y_old,x,y,"white")
  x_old,y_old=x,y
kandinsky.draw_string("Euler's Spiral",20,20,"white","black")
    
