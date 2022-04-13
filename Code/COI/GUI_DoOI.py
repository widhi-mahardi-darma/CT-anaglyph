import tkinter
import cv2
import numpy as np
import scipy.ndimage as ndi
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from tkinter import filedialog, messagebox


# Layout
width  = 770
height = 1260
display= tkinter.Tk()
display.minsize(width=width, height=height)
display.resizable(True,True)

# diketahui
x_image='' ; nilai_CoM='' ; canvas=''
nilai_CoM = [] ; Fit=[] ; y=''

def image (): # image
    global x_image, output

    #TODO: Clear Crart
    if output:
        for child in canvas.winfo_children():
            child.destroy()
    output = None
    nilai_CoM.clear()

    #Input data
    path_image = filedialog. \
        askopenfilename(multiple=True, initialdir="/", title="Open Image",
                        filetypes=(
                            ("Image", "*.tiff"), ("Image", "*.tif"),
                            ('Image', "*.bmp"), ("Image", "*.jpg"),
                            ("Image", "*.png"), ("Image", "*.txt")
                        ))

    # split image
    var = display.tk.splitlist(path_image)
    image = []

    # jumlah banyak citra
    x_image = len(var)
    print("jumlah image:", x_image)

    # List image
    for f in var:
        a = cv2.imread(f)
        image.append(a)

    # Center of Intensity
    for x in range(x_image):
        img= image[x]
        #center of intensity
        cy, cx, _ = ndi.center_of_mass(img)
        nilai_CoM.append(int(cx))

    '''----------------Plot-----------------'''
    y= np.array(nilai_CoM)
    x = np.arange(0.0, x_image, 1.0)
    # fig
    fig = Figure(figsize=(7.1, 5), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y, color='blue', label='COI')  # Biru
    plot1.legend()
    plot1.grid()

    output = FigureCanvasTkAgg(fig,master=canvas)
    output.draw()

    # placing the canvas on the Tkinter window
    output.get_tk_widget().pack()

def File(): # sinogram
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

    for i in range(x_image):
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
    x = np.arange(0.0, x_image, 1.0)

    fig = Figure(figsize=(7, 5), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    plot1.plot(x, y, color='blue', label='COI')  # Biru
    plot1.legend()
    plot1.grid()

    output = FigureCanvasTkAgg(fig,master=canvas)
    output.draw()

    # placing the canvas on the Tkinter window
    output.get_tk_widget().pack()


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
    global output

    # TODO: Clear Crart
    if output:
        for child in canvas.winfo_children():
            child.destroy()
    output = None
    #Grafik
    y= np.array(nilai_CoM)
    x = np.arange(0.0, x_image, 1.0)

    # Input data Fitting
    Amplitudo = float(amplitudo.get())
    Frekuensi= float(frekuensi.get())
    Phase=float(phase.get())
    Constanta= float(constanta.get())

    for i in range (x_image):
        Sin=math.sin(Frekuensi*i+Phase)
        fitting=Amplitudo*Sin+Constanta
        Fit.append(fitting)
    Y=np.array(Fit)

    fig = Figure(figsize=(7, 5), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    plot1.plot(x, Y, color='red', label='Fitting Model')  # Merah
    plot1.plot(x, y, color='blue', label='COI')  # Biru
    plot1.legend()
    plot1.grid()

    output = FigureCanvasTkAgg(fig, master=canvas)
    output.draw()

    # placing the canvas on the Tkinter window
    output.get_tk_widget().pack()

    Fit.clear()

# Menubar
Menu=tkinter.Menu(display)
display.config(menu=Menu)
output = None
fig = None

# Label frame
label_frame_1= tkinter.LabelFrame(display,
                                  width=725, height=510) #for aspect ratio 4:3
label_frame_1.pack(side=tkinter.LEFT)
label_frame_1.place (x=22.5, y=0)

canvas = tkinter.Canvas(display, width=710, height=500, bg='white')
canvas.pack(side=tkinter.LEFT)
canvas.place(x=27.5, y=3)

# Create menu
file_menu= tkinter.Menu(Menu)
Menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=image)
#file_menu.add_command(label ='Save', command=image)

# button Plot
plot_button = tkinter.Button(master = display, command = plot, height = 2,
                             width = 10, text = "Plot")
plot_button.place(x=470, y=610)

# button Jangkuan
jangkauan = tkinter.Button(master = display, command = Derajat, height = 2,
                             width = 20, text = "Derajat Jangkuan")
jangkauan.place(x=470, y=710)


#TODO: Input data Plot
'''Amplitudo'''
text_amplitudo = tkinter.Label(display, text="Amplitudo")
text_amplitudo.place(x=40, y=600)
amplitudo = tkinter.Entry(display, width=10)
amplitudo.place(x=40, y=625)
amplitudo.insert(0, round(20,5))

'''Phase'''
text_phase = tkinter.Label(display, text="Phase")
text_phase.place(x=260, y=600)
phase = tkinter.Entry(display, width=10)
phase.place(x=260, y=625)
phase.insert(0, round(1.01,5))

'''Frekuensi'''
text_frekuensi = tkinter.Label(display, text="Frekuensi")
text_frekuensi.place(x=150, y=600)
frekuensi = tkinter.Entry(display, width=10)
frekuensi.place(x=150, y=625)
frekuensi.insert(0, round(0.01,5))

'''Constanta'''
text_Constanta = tkinter.Label(display, text="Constanta")
text_Constanta.place(x=370, y=600)
constanta = tkinter.Entry(display, width=10)
constanta.place(x=370, y=625)
constanta.insert(0, round(200,5))

'''Frame'''
text_Frame = tkinter.Label(display, text="Frame")
text_Frame.place(x=40, y=700)
Frame = tkinter.Entry(display, width=10)
Frame.place(x=40, y=725)
Frame.insert(0, round(360,3))





# Layout
display.title("COI")
display.mainloop()