import kandinsky
import numpy as np

def f_to_plot(x,y):
    r = np.sqrt(x**2 + y**2)
    y = np.sin(r) / r
    return y
    
Nx = 220
Ny = 50
zscale= 150
xrange = (-12, 12)
yrange = (-12, 12)
# Ny*xshift + Nx = 310
# => xshift = (310 - Nx) / Ny
xshift = (300 - Nx) / Ny
yshift = xshift

kandinsky.fill_rect(0, 0, 320, 240, "black")
x_array = np.linspace(xrange[0], xrange[1], Nx)
for v in range(Ny):
    y = yrange[0] + (yrange[1] - yrange[0]) * v / (Ny - 1)
    z_array = f_to_plot(x_array, y)
    dx = v * xshift
    dy = v * yshift
    for h in range(Nx):
        x_screen = int(h + dx + 10)
        y_screen = int(200 - (z_array[h] * zscale + dy))
        kandinsky.set_pixel(x_screen, y_screen, "white")



