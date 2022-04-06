import tkinter
import cv2

import numpy as np
from matplotlib.backend_bases import key_press_handler
import scipy.ndimage as ndi
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt    


# Layout
width  = 770
height = 1260
display= tkinter.Tk()
display.minsize(width=width, height=height)
display.resizable(True,True)

# diketahui
x_image=''
nilai_CoM=''
plot1=''
Y=''
canvas=''
nilai_CoM = []
Fit=[]


def File():
    global x_image
    path_image = filedialog. \
        askopenfilename(initialdir="/", title="Image Left",
                        filetypes=(
                            ("Image", "*.tiff"), ("Image", "*.tif"),
                            ('Image', "*.bmp"), ("Image", "*.jpg"),
                            ("Image", "*.png"), ("Image", "*.txt")
                        ))

    image = cv2.imread(path_image,cv2.COLOR_BGR2GRAY)

    # shape
    y_image, x_image = image.shape
    print(image.shape)

    for i in range(x_image - 1):
        # image 1
        image1 = image[0: y_image + 0, x_image - (x_image - i): i + 1 + 0]

        m, n = image1.shape
        cv2.imwrite('image1.tiff', image1)

        # image 1
        img = cv2.imread('image1.tiff')

        cy, cx, _ = ndi.center_of_mass(img)
        nilai_CoM.append(int(cy))
    #Grafik
    y= np.array(nilai_CoM)
    x = np.arange(0.0, x_image-1, 1.0)

    fig = Figure(figsize=(7, 5), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    plot1.plot(x, y, '--', color='blue', label='COI')  # Biru
    plot1.legend()
    plot1.grid()

    canvas = FigureCanvasTkAgg(fig,master=display)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   display)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    plt.close('all')

def Derajat():

    Frekuensi = float(frekuensi.get())
    frame = float(Frame.get())

    # TODO: Frame,Radian and derajat
    '''Rad'''
    text_Radian = tkinter.Label(display, text="Radian")
    text_Radian.place(x=150, y=700)
    rad = Frekuensi * frame
    rad_entry = tkinter.Entry(display, width=10)
    rad_entry.place(x=150, y=725)

    rad_entry.delete(0, tkinter.END)
    rad_entry.insert(0, round(rad,3))

    '''derajat'''
    text_derajat = tkinter.Label(display, text="derajat")
    text_derajat.place(x=260, y=700)
    derajat = 180 * rad / math.pi

    derajat_entry = tkinter.Entry(display, width=10)
    derajat_entry.place(x=270, y=725)

    derajat_entry.delete(0, tkinter.END)
    derajat_entry.insert(0, round(derajat,3))


def plot():
    global Fit
    global nilai_CoM
    global x_image
    global plot1

    #Grafik
    y= np.array(nilai_CoM)
    x = np.arange(0.0, x_image-1, 1.0)

    # Input data Fitting
    Amplitudo = float(amplitudo.get())
    Frekuensi= float(frekuensi.get())
    Phase=float(phase.get())
    Constanta= float(constanta.get())

    for i in range (x_image-1):
        Sin=math.sin(Frekuensi*i+Phase)
        fitting=Amplitudo*Sin+Constanta
        Fit.append(fitting)
    Y=np.array(Fit)

    plt.plot(x,Y, color='red', label='Fitting Model') # Merah
    plt.plot(x, y, '--', color='blue', label='COI') # Biru
    plt.legend()
    plt.grid()
    plt.show()

    Fit.clear()

# Menubar
Menu=tkinter.Menu(display)
display.config(menu=Menu)

# Label frame
label_frame_1= tkinter.LabelFrame(display,
                                  width=725, height=510) #for aspect ratio 4:3
label_frame_1.pack(side=tkinter.LEFT)
label_frame_1.place (x=22.5, y=0)

# Create menu
file_menu= tkinter.Menu(Menu)
Menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=File)
# file_menu.add_command(label ='Save', command=Save)

# button that displays the plot
plot_button = tkinter.Button(master = display, command = plot, height = 2,
                             width = 10, text = "Plot")

# place the button
# in main window
plot_button.place(x=470, y=610)

# button that displays the plot
jangkauan = tkinter.Button(master = display, command = Derajat, height = 2,
                             width = 20, text = "Derajat Jangkuan")

# place the button
# in main window
jangkauan.place(x=470, y=710)


#TODO: Input data Plot
'''Amplitudo'''
text_amplitudo = tkinter.Label(display, text="Amplitudo")
text_amplitudo.place(x=40, y=600)
amplitudo = tkinter.Entry(display, width=10)
amplitudo.place(x=40, y=625)

'''Phase'''
text_phase = tkinter.Label(display, text="Phase")
text_phase.place(x=260, y=600)
phase = tkinter.Entry(display, width=10)
phase.place(x=260, y=625)

'''Frekuensi'''
text_frekuensi = tkinter.Label(display, text="Frekuensi")
text_frekuensi.place(x=150, y=600)
frekuensi = tkinter.Entry(display, width=10)
frekuensi.place(x=150, y=625)

'''Constanta'''
text_Constanta = tkinter.Label(display, text="Constanta")
text_Constanta.place(x=370, y=600)
constanta = tkinter.Entry(display, width=10)
constanta.place(x=370, y=625)

'''Frame'''
text_Frame = tkinter.Label(display, text="Frame")
text_Frame.place(x=40, y=700)
Frame = tkinter.Entry(display, width=10)
Frame.place(x=40, y=725)



# Layout
display.title("COI")
display.mainloop()