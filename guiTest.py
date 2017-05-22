import tkinter
import random
from tkinter import *

root = tkinter.Tk()
frame = Frame(root)
frame.pack()

def buttonClick():
    print(random.random())
    
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

sinButton = Button(frame, command = buttonClick, text="Sin(x)", fg="red")
sinButton.pack( side = LEFT)

cosButton = Button(frame, command = buttonClick, text="Cos(x)", fg="brown")
cosButton.pack( side = LEFT )

eButton = Button(frame, command = buttonClick, text="e^(x)", fg="blue")
eButton.pack( side = LEFT )

lnButton = Button(bottomframe, command = buttonClick, text="ln(x)", fg="black")
lnButton.pack( side = BOTTOM)

arcTanButton = Button(bottomframe, command = buttonClick, text="arctan(x)", fg="blue")
arcTanButton.pack( side = BOTTOM)

arcSinButton = Button(frame, command = buttonClick, text="arcsin(x)", fg="blue")
arcSinButton.pack( side = LEFT)

arcCosButton = Button(frame, command = buttonClick, text="arccos(x)", fg="blue")
arcCosButton.pack( side = LEFT)

root.mainloop()
