# convert number from one base to another base

sym = [str(n) for n in range(0,10)]+[chr(n) for n in range(65,91)]
sym = "".join(sym)

# convert number to base 10
# s: string representation of number
# base: integer stating number base of s
# returns: integer version of s in base 10
def tobase10(s, base):
  x=0
  for n in range(len(s)):
    ch=s[len(s)-n-1].upper()
    pos=sym[:base].rfind(ch)
    if pos>-1:
      x+=pos*base**n
    else:
      raise Exception("Invalid symbol '{0}' in '{1}' for base {2}".format(ch,s,base))
  return x

# convert number from base 10 to another base
# x: integer representation of number
# base: integer stating number base to convert to
# returns: string representation of x in new base
def frombase10(x, base):
  if not 2<=base<=35:
    raise Exception("<Specified number base outside range of 2..{0}".format(len(sym)-1))
  q=x
  value=""
  while q>0:
    q,r=divmod(q,base)
    value=sym[r]+value
  return value

print("Convert number from\none base to another")
print("For example\nhexadicimal -> base 16\nbinary -> base 2\ndecimal base 10\noctal -> base 8")
base_from=int(input("current base of number? "))
n=input("number value in base {0}? ".format(base_from))
base_to=int(input("base to convert to? "))
n_b10=tobase10(n,base_from)
n_result=frombase10(n_b10,base_to)
print("\n{0} in base {1} = {2} in base {3}".format(n,base_from,n_result,base_to))
print("in base 10 the value is {0}".format(n_b10))
