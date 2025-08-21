# numerically solve differential equation
# dy/dx = f(x,y)
# using Runge-Kutta
# and draw slope field
from math import *
import matplotlib.pyplot as plt

math_fun_dict = {   
  "pi": pi, "e": e, "sqrt": sqrt,
  "log": log, "exp": exp, "log10": log10,
  "sin": sin, "cos": cos, "tan": tan,
  "asin": asin, "acos": acos, "atan": atan,
  "abs": abs, "pow": pow
  }

# calculate value for derivative dy/dx using 
# given expression and supplied values for x and y
def eval_dy_dx(x_value, y_value):
    global_dict = { "x": x_value, "y": y_value, "__builtins__": {}}
    global_dict.update(math_fun_dict)
    dy_dx = eval(dy_dx_expr, global_dict)
    return dy_dx

# calculate solution for ODE based on initial values
# using Runge-Kutta method
def calc_rungekutta(print_values = True):
    x_list = []; y_list = []
    x = x_start
    y = y_start
    if print_values:
        print("{0:<8} {1:<13}".format("x","y"))
    for _ in range(n_steps):
        if print_values:
            print("{0:<8.6f} {1:<13.12f}".format(x,y))
        y_list.append(y)
        x_list.append(x)
        k1 = eval_dy_dx(x,y)
        k2 = eval_dy_dx(x + h / 2,y + h * k1 / 2)
        k3 = eval_dy_dx(x + h / 2,y + h * k2 / 2)
        k4 = eval_dy_dx(x + h,y + h * k3)
        y += h / 6 * (k1 + 2*k2 + 2*k3 + k4)
        x += h
    return [x_list,y_list]


# draw the slope field of dy_dx on the same plot als the solution
def draw_slope_field():
    ymax = max(y_list)
    ymin = min(y_list)
    nstep = 6
    xstep = (x_stop-x_start) / nstep
    ystep = (ymax-ymin) / nstep
    y = ymin
    for _ in range(nstep + 1):
        x = x_start
        for _ in range(nstep + 1):
            try:
                slope = eval_dy_dx(x, y)
            except ValueError:
                continue
            else:
                dx = xstep / 6
                dy = slope * dx
                plt.arrow(x - dx, y - dy, 2 * dx, 2 * dy,
                          color = "red", length_includes_head=True,
                          head_width = dx / 20)
            finally:
                x += xstep
        y += ystep

print("Can be used:")
for number, item in enumerate(math_fun_dict, 1):
    print(item, end=" ")
    if number % 3 == 0:
        print()
print("\nFor example\n-y/5 or -x**2")

# get inputs
dy_dx_expr = input("\ndy/dx = ")
n_steps = int(input("number of steps = "))
x_start = float(input("lowest value of x ="))
x_stop = float(input("highest value of x ="))
y_start = float(input("start value of y ="))

# calculate Euler time step h
h = (x_stop - x_start) / n_steps
print("h = {0}".format(h))

# optionally print values
answer = input("Print values before plot? y/n ")
print_values = True if answer.lower() == "y" else False

# call runge kutta function
x_list, y_list = calc_rungekutta(print_values)

if print_values:
    input("Press Exe to plot")

# draw slope field
draw_slope_field()
# plot
plt.plot(x_list,y_list, color = "blue")
plt.grid(True)
plt.show()
