# recursive turtle drawing Sierpinsky Triangle
import turtle as tl

def midpoint(p1,p2):
  x1,y1=p1;x2,y2=p2
  return [(x1+x2)/2,(y1+y2)/2]

def triangle(p1,p2,p3,depth,c):
  tl.color(c)
  tl.speed(0)
  tl.penup()
  tl.goto(p1[0],p1[1])
  tl.pendown()
  tl.goto(p2[0],p2[1])
  tl.goto(p3[0],p3[1])
  tl.goto(p1[0],p1[1])
  if depth>0:
    pn12=midpoint(p1,p2)
    pn23=midpoint(p2,p3)
    pn31=midpoint(p3,p1)
    triangle(p1,pn12,pn31,depth-1,"red")
    triangle(p2,pn12,pn23,depth-1,"green")
    triangle(p3,pn23,pn31,depth-1,"blue")

size=110
tl.penup()
tl.goto(-size+10,90)
tl.write("recursively drawn")
tl.goto(-size,70)
tl.write("Sierpinsky Triangle")
tl.pensize(1)
tl.hideturtle()
triangle([-size,-size+10],[size,-size+10],[0,size//2+10],5,"black")

