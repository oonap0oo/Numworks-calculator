# bezier curves
import kandinsky

# draw a line between an two points
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

# draw boxes at the points given
# points is a list or tuple of (x,y)
def mark_points(points,col):
  for p in points:
    kandinsky.fill_rect(p[0]-2,p[1]-2,4,4,col)

# linear Bézier curve (just a straight line)
# defined by 2 points
# points is a list or tuple of (x,y)
# t is the position along the curve 0<=t<=1
def bezier1(points,t):
  p0,p1=points
  x=(1-t)*p0[0]+t*p1[0]
  y=(1-t)*p0[1]+t*p1[1]
  return (int(x),int(y))

# Quadratic Bézier curve, defined by 3 points
# points is a list or tuple of (x,y)
# t is the position along the curve 0<=t<=1
def bezier2(points,t):
  p0,p1,p2=points
  x=(1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t**2*p2[0]
  y=(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t**2*p2[1]
  return (int(x),int(y))

# Cubic Bézier curves, defined by 4 points
# points is a list or tuple of (x,y)
# t is the position along the curve 0<=t<=1
def bezier3(points,t):
  p0,p1,p2,p3=points
  x=(1-t)**3*p0[0]+3*(1-t)**2*t*p1[0]+3*(1-t)*t**2*p2[0]+t**3*p3[0]
  y=(1-t)**3*p0[1]+3*(1-t)**2*t*p1[1]+3*(1-t)*t**2*p2[1]+t**3*p3[1]
  return (int(x),int(y))

# draw any of the bezier curves by specifying the bezier function
# funct_bezier: either bezier1(), bezier2() or bezier3()
# points is a list or tuple of (x,y)
# Nsteps: number of points calculated, are connected with straight lines
# col: color to draw
def draw_bezier(funct_bezier,points,Nsteps,col):
  for k in range(Nsteps):
    t=k/(Nsteps-1)
    x,y=funct_bezier(points,t)
    if k==0:
      kandinsky.set_pixel(x,y,col) # first point gets a single dot
    else:
      connect(xold,yold,x,y,col) # other points connected with line
    xold,yold=x,y

def demo():
  pa=(10,10)
  pb=(300,60)
  pc=(10,160)
  pd=(300,210)
  mark_points((pa,pb,pc,pd),"black")
  draw_bezier(bezier2,(pa,pb,pd),50,"red")
  kandinsky.draw_string("Quadratic Bézier curve",90,3,"red","white")
  draw_bezier(bezier3,(pa,pb,pc,pd),50,"blue")
  kandinsky.draw_string("Cubic Bézier curve",30,190,"blue","white")

demo()
