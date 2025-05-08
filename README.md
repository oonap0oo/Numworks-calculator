# Numworks-calculator
Python code made to run on a Numworks calculator

Also find these on [https://my.numworks.com/python/vnap0v](https://my.numworks.com/python/vnap0v)

## sierpinsky.py

![sierpinski_screenshot.png](sierpinski_screenshot.png)

Tested on the calculator using software version 23.2.6. Draws a Sierpinsky triangle on the screen. Defines one function sierp(), this function can be used with 1 parameter defining the number of iterations. Uses libraries math and kandinsky.

## logistic2.py

![logistic2_screenshot.png](logistic2_screenshot.png)

Tested on the calculator using software version 23.2.6. Function logistic_map() draws the bifurcation diagram of the logistic map on the screen. Uses libraries math and kandinsky. Can be used with 2 parameters logistic_map(astart, aend)

## tree.py

![tree_screenshot.png](tree_screenshot.png)

Tested on the calculator using software version 23.2.6. This program draws a tree using recursive function calls. It uses the turtle module for the drawing.

## graph_3d.py

![graph_3d_screenshot.png](graph_3d_screenshot.png)

This program draws a 3D plot. The function to plot is defined in f_to_plot(x,y). The matplotlib version on the calculator only has 2D capability. This program also has to function within memory which is allocated to Python on the calculator. Tested on the calculator using software version 23.2.6.

## graph3d_kandinsky.py
![graph3d_kandinsky_screenshot.png](graph3d_kandinsky_screenshot.png)

This program draws a 3D plot. The function to plot is defined in f_to_plot(x,y). This version uses the kandiinsky module. Tested on the calculator using software version 23.2.6.

## sphere.py
![sphere_screenshot.png](sphere_screenshot.png)

This code draws a rotating sphere using the kandinsky module. It also uses the sleep function of the time module and sin(), cos() from the math module. Tested on the calculator using software version 23.2.6.

## heron.py

![heron_screenshot.png](heron_screenshot.png)

Tested on the calculator using software version 23.2.6. Defines a function heronarea() which calculates the area of a triangle in terms of the three side lengths. The function can be called with the three lengths as parameters or without parameters. This code can run on CPython as well.

## bal.py

![bal_screenshot.png](bal_screenshot.png)

Tested on the calculator using software version 23.2.6. This code tests the matplotlib library of the calculator. It plots ballistic trajectories for a series of different starting angles. It uses libraries math, numpy and matplotlib.pyplot. This code can run on CPython as well.

## rpn.py

![rpn_screenshot.png](rpn_screenshot.png)

This script implements a simple Reverse Polish Notation calculator. 
Numbers are entered on the stack before the operators. 
For example 
```
5*6=
```
would here be entered as 
```
5 [Exe] 6 [Exe] * [Exe]
```
Tested on the calculator using software version 23.2.6
