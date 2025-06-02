values=[
  ("black",0),
  ("brown",1),
  ("red",2),
  ("orange",3),
  ("yellow",4),
  ("green",5),
  ("blue",6),
  ("violet",7),
  ("grey",8),
  ("white",9)
  ]
# shallow copy to avoid modifying the original
multipliers=values.copy()
multipliers.extend([
  ("gold",-1),
  ("silver",-2)
  ])
tolerances=[
  ("silver",10),
  ("gold",5),
  ("brown",1),
  ("red",2),
  ("green",0.5),
  ("violet",0.1)
  ]
prefixes={
  -3:"m",
  3:"k",
  6:"M",
  9:"G"
  }

def colorcode_value():
  print("Value bands:")
  char="\t"
  for v in values:
    print("{0} - {1:>8}".format(v[1],v[0]), end=char)
    char="\n" if char=="\t" else "\t"
  print("Enter numbers corresponding to\nall of the 2 or 3 value rings")
  val=int(input("Example: brown-black -> 10\nyellow-violet-black -> 470\n?"))
  print("Multiplier band:")
  char="\t"
  for k,v in enumerate(multipliers):
    print("{0} - {1:>8}".format(k,v[0]), end=char)
    char="\n" if char=="\t" else "\t"
  mul=multipliers[int(input("Enter number corresponding to\n multiplier ring:\n?"))]
  print("Tolerance band:")
  char="\t"
  for k,v in enumerate(tolerances):
    print("{0} - {1:>8}".format(k,v[0]), end=char)
    char="\n" if char=="\t" else "\t"
  tol=tolerances[int(input("Enter number corresponding to\n tolerance ring:\n?"))]
  res=float(str(val)+"E"+str(mul[1]))
  prefix_sci=3*((mul[1]+2)//3)
  factor=10**(mul[1]-prefix_sci)
  val*=factor
  prefix=prefixes.get(prefix_sci,"")
  print("value is {0:.2f} {1}Ohm".format(val,prefix))
  if prefix!="":
    print("or {0:.1f} Ohm".format(res))
  print("tolerance is {0} %".format(tol[1]))

colorcode_value()
