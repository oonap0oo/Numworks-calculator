from math import *
def heronarea(a=0,b=0,c=0):
  t1="s=0.5*(a+b+c)"
  t2="A=sqrt(s*(s-a)*(s-b)*(s-c))"
  print("Herons formula for area of a triangle\n"+t1+"\n"+t2)
  if a==0:
    sides=[];txt=("a","b","c")
    for i in range(3):
      inp=input("length of side "+txt[i]+"? ")
      sides.append(float(inp))  
  else:
    sides=[a,b,c]
  s=sum(sides)/2
  A=1
  for side in sides:
    A*=(s-side)
  if s*A<0:
    print("not a valid triangle")
    return 
  A=sqrt(s*A)
  print("Area A = "+str(A))
  return A
  
heronarea()
