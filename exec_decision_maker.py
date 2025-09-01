import kandinsky,random,time,ion

# define decision text and coordinates
options=(("DEFINITELY",30,60),
         ("ASK AGAIN",190,60),
         ("NEVER",30,90),
         ("FORGET IT",190,90),
         ("WHY NOT",30,120),
         ("POSSIBLY",190,120))
# draw the fixed text
def draw_text():
  kandinsky.fill_rect(0,0,320,240,"white")
  kandinsky.draw_string("EXECUTIVE DECISION MAKER",40,10,"black")
  kandinsky.draw_string("Press <Exe> to make decision",20,180,"black")

# draw options with 
# one highlighted
def draw_options(chosen):
  for index, option in enumerate(options):
    txt, x, y = option
    col = "red" if index == chosen else "black"
    kandinsky.fill_rect(x-8,y-3,115,25,col)
    kandinsky.draw_string(txt,x,y,"white",col)

# make a decisions with 
# some animation
def random_action():
  # random switching
  for _ in range(15):
    n=random.randrange(0,6)
    draw_options(n)
    time.sleep(0.2)
  # make chosen decsion
  # flicker for a while
  for _ in range(5):
    draw_options(7)
    time.sleep(0.1)
    draw_options(n)
    time.sleep(0.1)    
  return n

draw_text()
draw_options(7)
while True:
  if ion.keydown(ion.KEY_EXE):
    random_action()
