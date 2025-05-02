import matplotlib.pyplot as plt
import numpy as np

def f_to_plot(x,y):
    r = np.sqrt(x**2 + y**2)
    y = np.sin(r) / r
    return y
    
Nx = 30
Ny = 15
xrange = (-12, 12)
yrange = (-12, 12)
xshift = 0.8
yshift = 0.075

x_array = np.linspace(xrange[0], xrange[1], Nx)
for i in range(Ny):
    y = yrange[0] + (yrange[1] - yrange[0]) * i / (Ny - 1)
    z = f_to_plot(x_array, y)
    dx = i * xshift
    dy = i * yshift
    plt.plot(x_array + dx, z + dy, color="red")
plt.show()

