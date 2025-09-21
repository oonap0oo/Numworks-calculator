# Koch Snowflake and Antisnowfalke
import turtle as tl

# draw a Koch Curve using recursion
# is used for 1 side of the figure
def draw_koch_curve(length, recursion_depth,
                    draw_anti_snowflake = False):
  if recursion_depth > 0:
    length_3 = length / 3
    draw_koch_curve(length_3, recursion_depth - 1,
                    draw_anti_snowflake)
    tl.left(-60 if draw_anti_snowflake else 60)
    draw_koch_curve(length_3, recursion_depth - 1,
                    draw_anti_snowflake)
    tl.right(-120 if draw_anti_snowflake else 120)
    draw_koch_curve(length_3, recursion_depth - 1,
                    draw_anti_snowflake)
    tl.left(-60 if draw_anti_snowflake else 60)
    draw_koch_curve(length_3, recursion_depth - 1,
                    draw_anti_snowflake)
  else:
    tl.forward(length)

# draw the complete snowflake or antisnowflake
# uses function draw_koch_curve()
def draw_koch_snowflake(center_xy, length_side,
                        recursion_depth,
                        draw_anti_snowflake = False):
  xc, yc = center_xy
  y_upper = yc + length_side *0.5
  tl.penup()
  tl.goto(xc, y_upper)
  tl.setheading(-60)
  tl.pendown()
  draw_koch_curve(length_side, recursion_depth,
                  draw_anti_snowflake)
  tl.right(120)
  draw_koch_curve(length_side, recursion_depth,
                  draw_anti_snowflake)
  tl.right(120)
  draw_koch_curve(length_side, recursion_depth,
                  draw_anti_snowflake)
  tl.penup()
  
# setup Turtle         
def init_turtle():
  tl.speed(0)
  tl.pensize(2)
  tl.hideturtle()
  tl.pencolor("blue")

init_turtle()
# draw text
tl.penup()
tl.goto(-155,75)
tl.write("Koch Snowflake  Antisnowflake")
# draw snowflake
draw_koch_snowflake((-80,0), 130, 4, False)
# rad antisnowflake
draw_koch_snowflake((70,-15), 160, 4, True)

