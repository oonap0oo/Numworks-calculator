# Truchet Tiles using Python & Turtle
import turtle as tl
import time

# parameters
tile_size = 10 # size of one side of square tile measured in pixels
color_fg = "black"
line_width = 1
time_delay_ms = 1500

#   tile numbers
#   ------------
#   Tile            number
#   up-left         1
#   up-right        2
#   down-right      3
#   down-left       4

# pattern definitions, which tile number goes where
pattern_X = (
  (2,4,3,4,4,2),
  (2,1,2,2,4,4),
  (3,4,4,2,2,4),
  (2,2,4,4,2,1),
  (4,2,2,4,3,4),
  (4,4,2,1,2,2)
  )
  
pattern_Y = (
  (1,3,4,2),
  (3,1,2,4),
  (2,4,3,1),
  (4,2,1,3)
  )

pattern_1 = (
  (4,2,4,2,1,3,1,3),
  (1,3,1,3,4,2,4,2),
  (3,1,3,1,2,4,2,4),
  (1,3,1,3,4,2,4,2),
  (3,1,3,1,2,4,2,4),
  (2,4,2,4,3,1,3,1),
  (4,2,4,2,1,3,1,3),
  (2,4,2,4,3,1,3,1),
  )

pattern_2 = (
  (3,4,2,1,3,4),
  (4,2,4,3,1,3),
  (2,4,1,2,3,1),
  (3,1,4,3,2,4),
    (1,3,1,2,4,2),
  (2,1,3,4,2,1)
  )

pattern_3 = (
  (1,2,1,2,4,2,3,4,1,3),
  (3,4,3,4,2,4,2,1,3,1),
  (1,2,1,2,4,2,4,3,1,3),
  (4,1,2,3,1,3,1,2,4,2),
  (1,4,3,2,4,2,4,3,1,3),
  (4,3,4,3,1,3,1,2,4,2),
  (2,1,2,1,3,1,3,4,2,4),
  (4,3,4,3,1,3,2,1,4,2),
  (2,1,2,1,3,4,3,4,3,4),
  (3,4,3,4,2,1,2,1,2,1)
  )

# patterns to draw
patterns = (pattern_1,
            pattern_2,
            pattern_3,
            pattern_Y,
            pattern_X
            )

# set up turtle
def init():
  tl.reset() # clear screen
  # set speed
  tl.speed(0) # fastest drawing speed
  # more settings
  tl.pensize(line_width)
  tl.hideturtle()
  tl.color(color_fg)

# draw a single tile specified by number; x_top, y_top is the top left corner
def drawtile(tile_number, x_top, y_top):
  # three points depend on tile number
  if tile_number==1:
      x1, y1 = x_top, y_top
      x2, y2 = x_top + tile_size, y_top
      x3, y3 = x_top, y_top - tile_size
  elif tile_number==2:
      x1, y1 = x_top + tile_size, y_top
      x2, y2 = x_top + tile_size, y_top - tile_size
      x3, y3 = x_top, y_top
  elif tile_number==3:
      x1, y1 = x_top + tile_size, y_top - tile_size
      x2, y2 = x_top, y_top - tile_size
      x3, y3 = x_top + tile_size, y_top
  elif tile_number==4:
      x1, y1 = x_top, y_top - tile_size
      x2, y2 = x_top, y_top
      x3, y3 = x_top + tile_size, y_top - tile_size
  # draw the triangular shape of tile
  tl.penup()
  tl.goto(x1,y1)
  tl.pendown()
  tl.goto(x2,y2)
  tl.goto(x3,y3)
  tl.goto(x1,y1)

# draw a pattern of tiles; pattern is tuple of tuples containing the rows and columns of tile numbers
def draw_pattern(pattern, x_top, y_top):
   for row_number, row in enumerate(pattern):
     y = y_top - tile_size * row_number
     for column_number, tile in enumerate(row):
       x = x_top + tile_size * column_number
       drawtile(tile, x, y)

# draw a pattern several times as specified
def repeat_pattern(pattern, number_of_rows, number_of_columns):
  init()
  x_top = -150
  y_top = 100
  width_pattern = len(pattern[0])
  height_pattern = len(pattern)
  for row in range(number_of_rows):
    y_top_pattern = y_top - row * height_pattern * tile_size 
    for column in range(number_of_columns):
      x_top_pattern = x_top + column * width_pattern * tile_size
      draw_pattern(pattern, x_top_pattern, y_top_pattern)



init()

for p in patterns:
  rows = 200 // tile_size // len(p)
  cols = 300 // tile_size // len(p[0])
  repeat_pattern(p, rows, cols)
  time.sleep(1)
  



   

