# define function to draw ellipse using Turtle graphics
# use this function to draw a python logo
import turtle as tl
from math import *

# turtle graphics does have circle but no ellipse
# this function draws ellipse
# a, b: size of ellipse
# direction: positive for counterclockwise, negative for clockwise
# keyword arguments:
# extent: part of ellipse to draw as angle in degrees
# npoints: number of steps to use
def ellipse(a, b , direction, **kwargs):
  def rotate(x, y, angle_deg): # rotate x,y point by angle
    angle_rad = radians(angle_deg)
    xr = dx * cos(angle_rad) - dy * sin(angle_rad)
    yr = dx * sin(angle_rad) + dy * cos(angle_rad)   
    return([xr, yr])
  # unpack keyword parameters if present
  extent = kwargs.get("extent", 360)
  npoints = kwargs.get("npoints", 100)
  # store current position and heading
  x_start, y_start = tl.pos()
  angle_start = tl.heading()
  # loop to draw ellipse
  for step in range(npoints):
    angle = step / npoints * extent
    dx = copysign(1, direction) * a * (cos(radians(angle)) - 1)
    dy = b * sin(radians(angle))
    dx, dy = rotate(dx, dy, angle_start - 90)
    tl.goto(x_start + dx, y_start + dy)
  # leave turtle at new correct heading after the ellipse drawing
  new_angle = angle_start + extent * copysign(1, direction)
  tl.setheading(new_angle)

# draw one half of python logo and a seperate circle for the eye
def draw_shape(color_shape):
  # draw the shape
  tl.color(color_shape)
  tl.pendown()
  tl.forward(30)
  ellipse(15,15,+1, extent = 90)
  tl.forward(51)
  ellipse(45 , 21, 1, extent=180)
  tl.forward(21)
  tl.left(90)
  tl.forward(36)
  ellipse(3,3, -1, extent = 180)
  tl.forward(60)
  ellipse(45, 21, 1, extent=  180)
  tl.forward(24)
  tl.left(90)
  tl.forward(32)
  ellipse(18, 18, -1, extent = 90)
  tl.forward(27)
  # draw the eye
  x_current, y_current = tl.pos()
  angle_current = tl.heading()
  tl.setheading(90 + angle_current)
  tl.penup()
  tl.forward(75)
  tl.left(90)
  tl.forward(18)
  tl.pendown()
  ellipse(4 ,4, +1)
  tl.penup()
  tl.goto(x_current, y_current)

def init():
  # set speed of turtle
  tl.speed(0)
  tl.pensize(4)

# parameters
color1 = "#3b77a8" # blue color
color2 = "#ffe05d" # yellow color

# set up turtle
init()

# draw the blue half
tl.penup()
tl.goto(-50,0)
tl.setheading(0)
draw_shape(color1)

# draw the yellow half
tl.penup()
x_cor, y_cor = tl.position()
tl.goto(x_cor+12,y_cor-10)
tl.pendown()
tl.setheading(180)
draw_shape(color2)

# draw text
tl.penup()
tl.goto(20,70)
tl.write("python")
tl.goto(20,50)
tl.write("using Turtle")



