import kandinsky
# size of display
columns=32 
rows=13
# colors used
colors=("black","brown","red","orange","green","blue","purple")
Ncolors=len(colors)
# two nested loops for cols and rows
for y in range(rows):
  im=y/(rows-1)*2.5-1.25
  for x in range(columns):
    re=x/(columns-1)*3.5-2.5
    # complex constant c depends
    # on position
    c=complex(re,im)
    z=0
    i=0
    while abs(z)<2 and i<15:
      z=z**2+c # mandelbrot iteration
      i+=1
    txt=hex(i)[-1] #take last digit of hex
    if txt=="f": #looks nicer this way
      txt="."
    col=colors[i%Ncolors]
    kandinsky.draw_string(txt,x*10,203-y*17,col,"white")
