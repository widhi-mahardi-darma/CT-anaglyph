'''
- python 3.9
- change image suquence 360 to image analgyph
- Spefikasi layar 768X1366 (potrait)
'''

import tkinter
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import tkinter
import tempfile
import os
import Gui
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

import File

global display

# Layout
width  = 770
height = 1260
display= tk.Tk()
display.minsize(width=width, height=height)
display.resizable(True,True)

# Label frame
label_frame_1= tkinter.LabelFrame(display, text='Image',
                                  width=674, height=505) #for aspect ratio 4:3
label_frame_1.pack(side=tkinter.LEFT)
label_frame_1.place (x=22.5, y=15)

label_frame_2= tkinter.LabelFrame(display, text='Result image',
                                  width=674,height=505) #for aspect ratio 4:3
label_frame_2.pack(side=tkinter.LEFT)
label_frame_2.place (x=22.5, y=569)


#Label
label = tkinter.Label(label_frame_1)
label.pack(side=tkinter.LEFT)
label.place(x=10, y=5)
label.grid_propagate(0)
label.columnconfigure(1, weight=1)

label2 = tkinter.Label(label_frame_2)
label2.pack(side=tkinter.LEFT)
label2.place(x=10, y=5)
label2.grid_propagate(0)
label2.columnconfigure(1, weight=1)




# Menubar
Menu=tkinter.Menu(display)
display.config(menu=Menu)

# Create menu
file_menu= tkinter.Menu(Menu)
Menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=File)

# Layout
display.title("CT Anaglyph")
display.mainloop()
