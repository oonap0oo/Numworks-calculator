from math import *
stack=[0,0,0,0]
names=("x","y","z","t")
def move(di):
  if di=="up":
    stack[1],stack[2],stack[3]=stack[0],stack[1],stack[2]
  elif di=="down":
    stack[1],stack[2],stack[3]=stack[2],stack[3],0  
def help():
  print("\nRPN  for  Numworks")
  print("d: drop, s:swap, c:clear")
  print("dup: duplicate x, q:quit")
  print("+:add, -:subtract, *:multiply")
  print("/:divide, **: x to power y")
  print("sqrt:sqr root, chs:+ to -")
  print("use exp,sin,cos,tan,")
  print("asin,acos,atan,log,log10")
  input("\nhit <EXE> key")
loop=True
while loop:
  print("\n--------------------------")  
  print("RPN  for  Numworks")
  print("h:help, q:quit")
  print("--------------------------")
  for i in range(3,-1,-1):
    print(names[i]+"> "+str(stack[i]))
  a=input().lower().strip()
  a=a.replace("()","")
  if a in "+-**":
    stack[0]=eval(str(stack[1])+a+str(stack[0]))   
    move("down") 
  elif a=="/":
    if stack[1]!=0:
        stack[0]=stack[1]/stack[0]
        move("down") 
    else:
        print("divide by zero")
  elif a=="sqrt":
    if stack[0]>=0:
        stack[0]=sqrt(stack[0])
  elif a=="chs":
    stack[0]=-stack[0]
  elif a in ("exp","sin","cos","tan","asin","acos","atan","log","log10"):
    stack[0]=eval(a+"("+str(stack[0])+")")
  elif a=="":
    move("up")
    stack[3]=stack[2]
  elif a=="h":
    help()
  elif a=="pi":
    move("up")
    stack[0]=pi
  elif a=="q":
    loop=False
  elif a=="dup":
    move("up")
    stack[0]=stack[1]
  elif a=="d":
    stack[0]=stack[1]
    move("down")
  elif a=="c":
    stack=[0,0,0,0]
  elif a=="s":
    stack[0],stack[1]=stack[1],stack[0]    
  else:
    try:
      value=float(a)
    except:
      print(a+" not a valid entry")
    else:
      move("up")
      stack[0]=value
