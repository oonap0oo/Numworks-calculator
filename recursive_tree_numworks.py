import turtle as tl
from time import *
from random import *

# parameters
title = "Recursive tree"
angle_deg = 25 # angle of a new branch compared to previous branch
length_start = 30 # length of the trunk which is first drawn 
length_factor = 4/5 # factor which shortens branches of each succesive recursion
recursion_depth = 7 # number of recursions
randomness_length = (0.6, 1.4) # the interval of random variation of the length of branches
randomness_angel = (0.7, 1.3) # the interval of random variation of the angle of ea new branch
time_delay_ms = 1000 # time period to drawing of next tree

# set up turtle
def init():
  tl.reset()
  tl.colormode(1.0)
  # set speed
  tl.speed(0) # fastest drawing speed
  tl.hideturtle()

  
# this function recursively calls itself, when recursion limit is not yet reached
# it draws a branch and calls itself twice after changing the heading
# when recursion limit is reached it draws a leaf
def branch(length, depth, width):
  if depth > 0:
    red_value = uniform(0.6,0.8)
    color_value = (red_value, red_value / 2, 0) # random variation of brown colors
    tl.pencolor(color_value)
    if width < 1:
      width = 1 # width is reduced at each recursive function call but may not be smaller then 1
    tl.pensize(width)
    tl.pendown()
    tl.forward(length) # draw new branch
    original_position = tl.pos()
    original_heading = tl.heading()
    tl.right(angle_deg * uniform(*randomness_angel))
    new_length = length * length_factor * uniform(*randomness_length) # length of next branch
    branch(new_length, depth - 1, width - 1) # recursive call of this function
    tl.penup()
    tl.goto(original_position)
    tl.setheading(original_heading)
    tl.left(angle_deg * uniform(*randomness_angel))
    tl.pendown()
    new_length = length * length_factor * uniform(*randomness_length) # length of next branch
    branch(new_length, depth - 1,  width - 1) # recursive call of this function
  else:
    # draw a leaf with random variation in size and color
    color_value = (0, uniform(0.5,1), uniform(0, 0.2))
    tl.color(color_value)
    tl.right(90)
    tl.pensize(2)
    tl.circle(randint(2,4))
  
# clear screen ans starts function branch() to draw new tree 
def draw_tree():
  tl.penup()
  tl.setheading(90)
  tl.goto(0,-100)
  branch(length_start, recursion_depth, recursion_depth) 
    

while True:
  init()
  draw_tree()
  sleep(1)

    
