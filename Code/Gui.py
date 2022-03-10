'''
- python 3.9
- change image suquence 360 to image analgyph
- Spefikasi layar 768X1366 (potrait)
'''

''' 
#1-3-2022
- menambahkan pilihan anaglip 2 citra
# 2-3- 2022
- menampilkan citra
- Mengganti jpg mejadi Image
# 4-3-2022
- Hasil save temp
# 7-3-2022
- membenarkan layout
# 8-3-2022
- menampilkan hasil citra analgpyh
#9-3-2022
-zoom to fit
#10-3-2022
-mencari kesalahan saat membaca output citra
'''

import tkinter as tk
import  numpy as np
import cv2
import tkinter
import tempfile
import os
import sys
import imutils
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
import PIL, PIL.Image, PIL.ImageOps, PIL.ImageEnhance


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

def File():

    path = tempfile.gettempdir()

    def Satu():

        # Upload Image L
        path_image = filedialog. \
            askopenfilename(initialdir="/", title="Image Left",
                            filetypes=(
                                ("Image", "*.tiff"), ("Image", "*.tif"),
                                ('Image', "*.bmp"), ("Image", "*.jpg"),
                                ("Image", "*.png"), ("Image", "*.txt")
                            ))

        global imgL
        imgL = PIL.Image.open(path_image, mode='r').convert('RGB')
        imgL = PIL.Image.open(path_image, mode='r').convert('L')

        # upload image R
        path_image = filedialog. \
            askopenfilename(initialdir="/", title="Image Right",
                            filetypes=(
                                ("Image", "*.tiff"), ("Image", "*.tif"),
                                ('Image', "*.bmp"), ("Image", "*.jpg"),
                                ("Image", "*.png"), ("Image", "*.txt")
                            ))

        global imgR
        imgR = PIL.Image.open(path_image, mode='r').convert('RGB')
        imgR = PIL.Image.open(path_image, mode='r').convert('L')
        display2.destroy()

        # Filter Color

        red_img = PIL.ImageOps.colorize(imgL, (0, 0, 0), (255, 0, 0))  # Red
        cyan_img = PIL.ImageOps.colorize(imgR, (0, 0, 0), (0, 255, 255))  # Image Cyan

        # Image Blendig Red and Cyan
        blend = PIL.Image.blend(red_img, cyan_img, 0.5)
        np_blend = np.array(blend)
        im_comb = imutils.resize(np_blend, height=600)
        im_comb = cv2.cvtColor(im_comb, cv2.COLOR_BGR2RGB)  # Hasil Anaglyph

        #image concatenate
        numpy_hor = np.concatenate((red_img, cyan_img), axis=1)
        numpy_hor = cv2.cvtColor(numpy_hor, cv2.COLOR_BGR2RGB)
        print(numpy_hor.shape)

        # shape image
        a,b,c=numpy_hor.shape

        #Shape
        cv2.imwrite(os.path.join(path,'Red an Cyan.tiff'), cv2.resize(numpy_hor, (0, 0), None, .7, .7))
        img_con= Image.open(os.path.join(path, 'Red an Cyan.tiff'))

        # menampilkan citra awal
        img_con = img_con.resize((int(b/1.7),int(a/1.7)), Image.ANTIALIAS)
        uu = ImageTk.PhotoImage(img_con)
        label.configure(image=uu)
        label.image = uu

        # Nama File yang save
        q, w,e = im_comb.shape
        cv2.imwrite(os.path.join(path, 'Anaglyph.tiff'), im_comb)
        img = Image.open(os.path.join(path, 'Anaglyph.tiff'))

        # menampilkan hasil citra
        img = img.resize((int(w/1.5), int(q/1.5)), Image.ANTIALIAS)
        uu = ImageTk.PhotoImage(img)
        label2.configure(image=uu)
        label2.image = uu

    def Dua():
        # Upload Image
        path_image = filedialog. \
            askopenfilename(multiple=True, initialdir="/", title="Image Left",
                            filetypes=(
                                ("Image", "*.tiff"), ("Image", "*.tif"),
                                ('Image', "*.bmp"), ("Image", "*.jpg"),
                                ("Image", "*.png"), ("Image", "*.txt")
                            ))

        # menunut display 2
        display2.destroy()

        #split image
        var=display.tk.splitlist(path_image)
        image=[]
        global jumlah_img

        # jumlah banyak citra
        jumlah_img=len(var)
        print("jumlah image:", jumlah_img)
        for f in var:
            a=cv2.imread(f)
            image.append(a)

        # input image
        #image_overlap=20

        for i in range(jumlah_img):

            # Image Left
            image_keL = i  # jumlah image input

            # Image Right
            image_keR = i + 20

            if image_keR >= jumlah_img :
                image_keR = image_keR - jumlah_img
                print('image L:>', image_keL, 'nomor',i)
                print('image R>:', image_keR)

                # Input image left (dibalik R ke L)
                global imgL
                cv2.imwrite(os.path.join(path, 'imgL.tiff'), image[image_keL])
                imgL = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff', mode='r').convert('RGB')
                imgL = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff', mode='r').convert('L')

                # Input image right (dan sebaliknya)
                global imgR
                cv2.imwrite(os.path.join(path, 'imgR.tiff'), image[image_keR])
                imgR = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff', mode='r').convert('RGB')
                imgR = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff', mode='r').convert('L')

                # Filter Color
                red_img = PIL.ImageOps.colorize(imgL, (0, 0, 0), (255, 0, 0))  # Red
                cyan_img = PIL.ImageOps.colorize(imgR, (0, 0, 0), (0, 255, 255))  # Image Cyan
                blend = PIL.Image.blend(red_img, cyan_img, 0.5)


            else:
                print('image L:', image_keL, 'nomor', i)
                print('image R:', image_keR)

                # Input image left
                cv2.imwrite(os.path.join(path, 'imgL.tiff'), image[image_keL])
                # cv2.imwrite(('Lllllxxxx'+str(i)+'.tiff'), image[image_keL])
                imgL = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff', mode='r').convert('RGB')
                imgL = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff', mode='r').convert('L')

                # Input image right
                cv2.imwrite(os.path.join(path, 'imgR.tiff'), image[image_keR])
                # cv2.imwrite(('Rrrrrrxxxx' + str(i) + '.tiff'), image[image_keR])
                imgR = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff', mode='r').convert('RGB')
                imgR = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff', mode='r').convert('L')

            # Image Blendig Red and Cyan
            # Filter Color
            red_img = PIL.ImageOps.colorize(imgL, (0, 0, 0), (255, 0, 0))  # Red
            cyan_img = PIL.ImageOps.colorize(imgR, (0, 0, 0), (0, 255, 255))  # Image Cyan
            blend = PIL.Image.blend(red_img, cyan_img, 0.5)

            np_blend = np.array(blend)
            im_comb = imutils.resize(np_blend, height=600)
            im_comb = cv2.cvtColor(im_comb, cv2.COLOR_BGR2RGB) # Hasil Anaglyph

            # image concatenate
            numpy_hor = np.concatenate((red_img, cyan_img), axis=1)
            numpy_hor = cv2.cvtColor(numpy_hor, cv2.COLOR_BGR2RGB)
            a,b,c=numpy_hor.shape
            cv2.imwrite(os.path.join(path, 'Red an Cyan.tiff'), cv2.resize(numpy_hor, (0, 0), None, .7, .7))
            img_con = Image.open(os.path.join(path, 'Red an Cyan.tiff'))

            # menampilkan citra awal
            img_con = img_con.resize((int(b / 1.7), int(a / 1.7)), Image.ANTIALIAS)
            uu = ImageTk.PhotoImage(img_con)
            label.configure(image=uu)
            label.image = uu

            # Nama File yang save
            global q; global w
            q1, w1, e = im_comb.shape
            file = 'Anaglyph'
            cv2.imwrite(os.path.join(path, file + str(i-1)) + '.tiff', im_comb)
            img = Image.open(os.path.join(path, 'Anaglyph' + str(1)) + '.tiff')

            #menampilkan hasil citra
            # Shape
            q=int(q1/1); w=int(w1/1)
            # menampilkan citra
            img = img.resize((w,q), Image.ANTIALIAS)
            uu = ImageTk.PhotoImage(img)
            label2.configure(image=uu)
            label2.image = uu

        def scale(value:None):
            global Over; global q; global w
            Over = (int(sequence.get()))
            path = tempfile.gettempdir()

            # Open Image
            img = Image.open(os.path.join(path, 'Anaglyph' + str(Over-1)) + '.tiff')

            # Shape Image
            q=int(q1/1);w=int(w1/1)

            # menampilkan citra scale
            img = img.resize((w, q), Image.ANTIALIAS)
            uu = ImageTk.PhotoImage(img)
            label2.configure(image=uu)
            label2.image = uu

        #Scale
        sequence = tkinter.Scale(display, from_=0, to=(jumlah_img-1), length=674,
                                 resolution=1, orient=tkinter.HORIZONTAL, command=scale)
        sequence.place(x=20, y=1075)


    # Display 2
    width = 350
    height = 250
    display2 = tk.Tk()
    display2.minsize(width=width, height=height)
    display2.resizable(True, True)

    #button
    # Button
    btn_pilihan1 = tkinter.Button(display2, text="1", width=10, command=Satu)
    btn_pilihan1.place(x=50, y=100)

    btn_pilihan2 = tkinter.Button(display2, text="2", width=10, command=Dua)
    btn_pilihan2.place(x=100, y=150)

    display2.title("Menu")
    display2.mainloop()

def Save():
    global lab_img
    global trim
    global nilai_pixel
    global nilai_unsharp
    global jumlah
    global filePaths

    file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='save image')

    for i in range(jumlah):
        path = tempfile.gettempdir()

        # hasil 8 bit menjadi 16 bit
        img = np.array(hasil, dtype=np.uint16)
        img = cv2.normalize(img, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)  # hasil 16 bit

        io.imsave((file + str(jumlah - i)) + '.tiff', img)
    messagebox.showinfo('Save', ' Semua citra telah tersimpan')


# Menubar
Menu=tkinter.Menu(display)
display.config(menu=Menu)

# Create menu
file_menu= tkinter.Menu(Menu)
Menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=File)
file_menu.add_command(label ='Save', command=Save)

# Layout
display.title("CT Anaglyph")
display.mainloop()
