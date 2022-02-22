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

# def File():
#     global jumlah
#     global filePaths
#     global rr, r
#     global ee, e
#     global label
#     global display
#
#     def scale(value=None):  # digunakan image sequence
#         global Over
#         Over = (int(overlapping.get()))
#
#         # Menampilkan citra
#         size = (int(r / rr), int(e / ee))
#         Tampil = cv2.resize(filePaths[Over], size, interpolation=cv2.INTER_AREA)
#         pillow_img = Image.fromarray(Tampil)
#         uu = ImageTk.PhotoImage(pillow_img)
#         label.configure(image=uu)
#         label.image = uu
#         path = tempfile.gettempdir()
#         cv2.imwrite(os.path.join(path, 'labCT.tiff'), filePaths[Over])
#
#     fln = filedialog.askopenfilename(multiple=True, initialdir="/", title="select file",
#                                      filetypes=(
#                                          ("tiff", "*.tiff"), ("tif", "*.tif"), ("bmp", "*.bmp"), ("jpg", "*.jpg"),
#                                          ("png", "*.png"), ("all file", "*.txt")))
#
#     var = display.tk.splitlist(fln)
#     filePaths = []
#
#     jumlah = len(var)
#     print('jumlah citra:', jumlah)
#
#     for f in var:
#         print(f)
#         a = cv2.imread(f)
#         filePaths.append(a)
#
#     awal = cv2.cvtColor(filePaths[0], cv2.COLOR_BGR2GRAY)
#
#     path = tempfile.gettempdir()
#     cv2.imwrite(os.path.join(path, 'labCT.tiff'), filePaths[0])
#
#     # untuk menampilkan UI
#     e, r = awal.shape
#
#     if r > 0 and r < 1799:
#         rr = 1.15
#         ee = 1.15
#
#     if r > 1800 and r < 3700:
#         rr = 3.05
#         ee = 2.55
#
#     if r > 3700 and r < 3899:
#         rr = 5.95
#         ee = 6.15
#
#     if r > 3900 and r < 5700:
#         rr = 6.3
#         ee = 6.15
#
#     if r > 5701:
#         rr = 9.55
#         ee = 10.25
#
#     size = (int(r / rr), int(e / ee))
#     Tampil = cv2.resize(filePaths[0], size, interpolation=cv2.INTER_AREA)
#     pillow_img = Image.fromarray(Tampil)
#     uu = ImageTk.PhotoImage(pillow_img)
#     label.configure(image=uu)
#     label.image = uu
#
#     overlapping = tkinter.Scale(display, from_=0, to=jumlah - 1, length=674,
#                                 resolution=1, showvalue=0, orient=tkinter.HORIZONTAL, command=scale)
#     overlapping.place(x=20, y=525)



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
