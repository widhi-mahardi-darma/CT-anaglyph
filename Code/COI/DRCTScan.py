from importlib.resources import path

import dxchange
import tomopy
import tkinter
import tkinter as tk
import cv2
import os
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import tkinter.font as tkFont
from tkinter import filedialog, Scale
import matplotlib.pyplot as plt
import tempfile
from skimage import io, img_as_float
from PIL import Image, ImageTk

'''''
1. belum dapat di slide 
2. belum disave di tamp
3. label belum pas
4. image processing bdelum bisa'''
Label=''
path_save=''
total_recon=''

class App:
    def __init__(self, root): # Display
        global Label

        ''''------Display--------'''
        root.title("DRCTScan")
        #setting window size
        width= 370
        height= 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(True,True)

        """-------------Open------------------"""
        Open_button=tk.Button(root)
        Open_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Open_button["font"] = ft
        Open_button["fg"] = "#000000"
        Open_button["justify"] = "center"
        Open_button["text"] = "Open File"
        Open_button.place(x=35,y=20,width=75,height=58)
        Open_button["command"] = self.Open_button_command

        """---------Interpolation------------------"""
        Interpolation_button=tk.Button(root)
        Interpolation_button["anchor"] = "center"
        Interpolation_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Interpolation_button["font"] = ft
        Interpolation_button["fg"] = "#000000"
        Interpolation_button["justify"] = "center"
        Interpolation_button["text"] = "Interpolate "
        Interpolation_button["relief"] = "raised"
        Interpolation_button.place(x=130,y=20,width=74,height=58)
        Interpolation_button["command"] = self.Interpolation

        """-----------------Recontruction---------------------"""
        Recon_button=tk.Button(root)
        Recon_button["anchor"] = "center"
        Recon_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Recon_button["font"] = ft
        Recon_button["fg"] = "#000000"
        Recon_button["justify"] = "center"
        Recon_button["text"] = "Reconstruction "
        Recon_button["relief"] = "raised"
        Recon_button.place(x=230,y=20,width=94,height=58)
        Recon_button["command"] = self.Recon_button_command

        """-----------------Save------------------------"""
        Save_button = tk.Button(root)
        Save_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Save_button["font"] = ft
        Save_button["fg"] = "#000000"
        Save_button["justify"] = "center"
        Save_button["text"] = "Save\n Recontruction"
        Save_button.place(x=340, y=20, width=94, height=58)
        Save_button["command"] = self.Save_Recontruction

        """-----------------COI------------------------"""
        COI_button = tk.Button(root)
        COI_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        COI_button["font"] = ft
        COI_button["fg"] = "#000000"
        COI_button["justify"] = "center"
        COI_button["text"] = "Center of Intensity"
        COI_button.place(x=600, y=20, width=120, height=58)
        COI_button["command"] = self.COI

        """"-------------------Label-----------------"""
        label_Frame= tk.LabelFrame(root, width=674, height=505)
        label_Frame.pack(side=tk.LEFT)
        label_Frame.place(x=40, y=100)
        Label=tk.Label(root)
        Label.pack(side=tk.LEFT)
        Label.place(x=42,y=102)
        Label.grid_propagate(0)
        Label.columnconfigure(1, weight=1)

        """-------------Citra------------------"""
        Citra_button = tk.Button(root)
        Citra_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Citra_button["font"] = ft
        Citra_button["fg"] = "#000000"
        Citra_button["justify"] = "center"
        Citra_button["text"] = "Citra"
        Citra_button.place(x=40, y=690, width=75, height=58)
        Citra_button["command"] = self.Citra

        """---------Sinogram------------------"""
        Sinogram_button = tk.Button(root)
        Sinogram_button["anchor"] = "center"
        Sinogram_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Sinogram_button["font"] = ft
        Sinogram_button["fg"] = "#000000"
        Sinogram_button["justify"] = "center"
        Sinogram_button["text"] = "Sinogram "
        Sinogram_button["relief"] = "raised"
        Sinogram_button.place(x=150, y=690, width=74, height=58)
        Sinogram_button["command"] = self.Sinogram

        """-----------------Save Hasil---------------------"""
        Save_Hasil_button = tk.Button(root)
        Save_Hasil_button["anchor"] = "center"
        Save_Hasil_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Save_Hasil_button["font"] = ft
        Save_Hasil_button["fg"] = "#000000"
        Save_Hasil_button["justify"] = "center"
        Save_Hasil_button["text"] = " Save\n Sinogram "
        Save_Hasil_button["relief"] = "raised"
        Save_Hasil_button.place(x=460, y=20, width=94, height=58)
        Save_Hasil_button["command"] = self.Save_Sinogram


    def Open_button_command(self):
        global proj; global Label
        global total_image; global slider

        save_temp=tempfile.gettempdir()

        #open Image
        img = filedialog.askopenfilename(multiple=True, initialdir='/', title='select file',
                                         filetypes=(
                                             ("Image", "*.tiff"), ("Image", "*.tif"),
                                             ('Image', "*.bmp"), ("Image", "*.jpg"),
                                             ("Image", "*.png"), ("Image", "*.txt")
                                         ))

        # Total image
        total_image = int(len(img))
        print('image',img)
        print('Total Image:',total_image)
        proj = dxchange.read_tiff_stack(img[0], range(0, total_image))

        '''----------Sinogram--------------'''
        cv2.imwrite(os.path.join(save_temp, 'sino.tiff'),proj[:, 0, :])
        dxchange.write_tiff(proj[:, 0, :], save_temp, overwrite=True)

        '''------menampilkan citra-----'''
        img = proj[0, :, :]
        print(img.shape)
        L_i, P_i = img.shape

        # Views
        img_view = np.array(img,dtype=np.uint8)
        img_view = cv2.normalize(img_view, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        img_view=cv2.resize(img_view, (int(P_i/2),int(L_i/2)), interpolation=cv2.INTER_AREA)
        img_view = Image.fromarray(img_view)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image=img_view

        '''----------Scale-----------'''
        def Scale(value:None):
            Scale=int(slider.get())
            print(Scale)
            plt.imshow(proj[Scale,:,:])
            img = proj[Scale,:,:]
            L_i, P_i= img.shape
            img_view = cv2.resize(img, (int(P_i / 2), int(L_i / 2)), interpolation=cv2.INTER_AREA)
            img_view = Image.fromarray(img_view)
            img_view = ImageTk.PhotoImage(img_view)
            Label.configure(image=img_view)
            Label.image = img_view

        #Slider
        slider = tk.Scale(root, from_=0, to=total_image-1, length=674,
                         resolution=1, orient=tkinter.HORIZONTAL, command=Scale)
        slider.place(x=40, y=617)

    def Interpolation(self):
        print("command")

    def Recon_button_command(self):
        global path_save; global recon; global total_recon
        path_temp=tempfile.gettempdir()

        '''-------Data--------'''
        data = proj
        data = tomopy.remove_nan(data, val=0.0)
        data = tomopy.remove_neg(data, val=0.00)
        data[np.where(data == np.inf)] = 0.00

        '''--------------Tomopy-------------------'''
        theta = tomopy.angles(data.shape[0], 0, 360)
        tomopy.write_center(data, theta, dpath='theta/Center', mask=True, ratio=.98, filter_name= 'ramlak')
        com = tomopy.find_center(data, theta, tol=0.1)
        a = np.mod(com, 1)
        print(f'Center of Mass :', com)

        options = {'proj_type': 'linear', 'method': 'FBP'}
        recon = tomopy.recon(data, theta, center=com, algorithm=tomopy.astra, options=options, ncore=1, filter_name= 'ramlak')
        recon = tomopy.circ_mask(recon, axis=0, ratio=0.95)

        '''----------Save temp------------------'''
        file = 'recon'
        total_recon = int(len(recon))
        print(f'total_recon :', total_recon)
        for i in range(total_recon):
            cv2.imwrite(os.path.join(path_temp, file + str((total_recon-1) - (i))) + '.tiff', recon[i, :, :])


    def Save_Recontruction(self):
        path_save = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Save Reconstructed Image')
        print(path_save)
        dxchange.write_tiff_stack(recon, path_save, overwrite=True)

    def COI (self):
        import COI

    def Citra (self):
        global slider_citra
        slider.destroy()

        path_temp = tempfile.gettempdir()

        #open Image
        image = Image.open(os.path.join(path_temp, 'recon1.tiff'))

        # Convert menjadi 8 bit
        na = np.array(image)
        img_view = cv2.normalize(na, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        img_view=(img_view*255).astype(np.uint8)

        #View
        img_view = cv2.resize(img_view, (400, 400), interpolation=cv2.INTER_AREA)
        img_view = Image.fromarray(img_view)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image = img_view

        def Scale(value: None):
            #Scale
            Scale = int(slider_citra.get())
            print(Scale)

            # Open Image
            image = Image.open(os.path.join(path_temp, 'recon' + str(Scale)) + '.tiff')

            # Convert menjadi 8 bit
            na = np.array(image)
            img_view = cv2.normalize(na, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            img_view = (img_view * 255).astype(np.uint8)

            # View
            img_view = cv2.resize(img_view, (400, 400), interpolation=cv2.INTER_AREA)
            img_view = Image.fromarray(img_view)
            img_view = ImageTk.PhotoImage(img_view)
            Label.configure(image=img_view)
            Label.image = img_view

        # Scale
        slider_citra = tk.Scale(root, from_=0, to=int(total_recon) - 1, length=674,
                          resolution=1, orient=tkinter.HORIZONTAL, command=Scale)
        slider_citra.place(x=40, y=617)

    def Sinogram(self):
        slider.destroy()
        slider_citra.destroy()

        save_temp = tempfile.gettempdir()
        img_sino = cv2.imread(os.path.join(save_temp,'sino.tiff'))

        # menampilkan citra Sinogram
        img_view = Image.fromarray(img_sino)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image = img_view

    def Save_Sinogram (self):
        path_save = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Save Reconstructed Image')
        print(path_save)
        cv2.imwrite(path_save+'.tiff',proj[:, 0, :])



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
