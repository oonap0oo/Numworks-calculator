from turtle import *

angle = 45
main_branch = 20
colors = ("green","yellow","orange","red","brown","black")

def draw(branch_size, branch_length):
    pensize(branch_size)
    color(colors[branch_size - 1])
    forward(branch_length)

def branch(depth):
    if depth > 0:
        h = heading()
        p = position()
        draw(depth, main_branch)
        branch(depth - 1)
        penup()
        goto(p)
        setheading(h + angle)
        pendown()
        draw(depth, main_branch // 2)
        branch(depth - 1)
        penup()
        goto(p)
        setheading(h - angle)
        pendown()
        draw(depth, main_branch // 2)
        branch(depth - 1)
    else:
        return()

setheading(90)
goto(0,-60)
speed(10)
hideturtle()
draw(6,main_branch + 10)
branch(5)
