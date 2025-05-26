V=None;I=None;R=None
def determine(x):
  global V,I,R
  x=x.upper()
  if x.endswith("V"):
    x=x.replace("V","")
    V=float(x)
    return "voltage"
  elif x.endswith("A"):
    x=x.replace("A","")
    I=float(x)
    return "current"
  elif x.endswith("OHM"):
    x=x.replace("OHM","")
    R=float(x)
    return "resistance"
 
def ohmlaw():
  global V,I,R
  print("Ohms law helper")
  print("Enter voltage or current")
  print("or resistance")
  print("ex. 5V or 0.1A or 1000Ohm")
  answer=input()
  vartype1=determine(answer)
  if vartype1=="voltage":
      answer=input("Enter current or resistance\n")
      vartype2=determine(answer)
      if vartype2=="current":
        R=V/I
        print("Resistance: ",R,"Ohm")
      elif vartype2=="resistance":
        I=V/R
        print("Current:",I,"A")            
  elif vartype1=="current":
      answer=input("Enter voltage or resistance\n")
      vartype2=determine(answer)
      if vartype2=="voltage":
        R=V/I
        print("Resistance:",R,"Ohm")
      elif vartype2=="resistance":
        V=R*I
        print("Voltage:",V,"V")                     
  elif vartype1=="resistance":
      answer=input("Enter voltage or current\n")        
      vartype2=determine(answer)
      if vartype2=="voltage":
        I=V/R
        print("Current:",I,"A")
      elif vartype2=="current":
        V=R*I
        print("Voltage:",V,"V")  

ohmlaw()


    
    
