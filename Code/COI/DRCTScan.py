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

'''''
1. belum dapat di slide 
2. belum disave di tamp
3. label belum pas
4. image processing bdelum bisa'''
Label=''
path_save=''

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
        Open_button.place(x=40,y=20,width=75,height=58)
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
        Interpolation_button.place(x=150,y=20,width=74,height=58)
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
        Recon_button.place(x=260,y=20,width=94,height=58)
        Recon_button["command"] = self.Recon_button_command

        """-----------------Save------------------------"""
        Save_button = tk.Button(root)
        Save_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Save_button["font"] = ft
        Save_button["fg"] = "#000000"
        Save_button["justify"] = "center"
        Save_button["text"] = "Save File"
        Save_button.place(x=380, y=20, width=75, height=58)
        Save_button["command"] = self.Save_button_command


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
        Save_Hasil_button["text"] = " Save Hasil "
        Save_Hasil_button["relief"] = "raised"
        Save_Hasil_button.place(x=260, y=690, width=94, height=58)
        Save_Hasil_button["command"] = self.Recon_button_command


    def Open_button_command(self):
        global proj
        global Label
        global total_image

        save_temp=tempfile.gettempdir()
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
        #plt.imshow(proj[:, 0, :])
        dxchange.write_tiff(proj[:, 0, :], save_temp, overwrite=True)
        #plt.show()  # sinogram


        img = proj[0,:,:]
        print(img.shape)
        L_i,P_i=img.shape


        # hasil 8 bit menjadi 16 bit
        # img_view = np.array(img, dtype=np.uint16)
        # img = cv2.normalize(img_view, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)  # hasil 16 bit

        img_view = np.array(img,dtype=np.uint8)
        img_view = cv2.normalize(img_view, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

        #img_view = cv2.cvtColor(img_view, cv2.COLOR_BGR2GRAY)

        img_view=cv2.resize(img_view, (int(P_i/2),int(L_i/2)), interpolation=cv2.INTER_AREA)
        img_view = Image.fromarray(img_view)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image=img_view

        def Scale(value:None):
            Scale=int(slider.get())
            print(Scale)
            plt.imshow(proj[Scale,:,:])
            img = proj[Scale,:,:]
            L_i, P_i= img.shape
            img_view = Image.fromarray(img)
            img_view = ImageTk.PhotoImage(img_view)
            Label.configure(image=img_view)
            Label.image = img_view

        # Scale
        slider = tk.Scale(root, from_=0, to=total_image-1, length=674,
                         resolution=1, orient=tkinter.HORIZONTAL, command=Scale)
        slider.place(x=40, y=617)


    def Interpolation(self):
        print("command")

    def Recon_button_command(self):
        global path_save
        path_temp=tempfile.gettempdir()
        hshift = 30
        vshift = 150



        data = proj

        #BELUM DAPAT DIGUNAKAN

        # sino = dxchange.read_tiff_stack(proj, range(1, 360))
        # plt.imshow(sino[:, 0, :])
        # dxchange.write_tiff(sino[:, 0, :], D, overwrite=True)
        # plt.show()  # sinogram

        data = tomopy.remove_nan(data, val=0.0)
        data = tomopy.remove_neg(data, val=0.00)
        data[np.where(data == np.inf)] = 0.00

        # dxchange.write_tiff_stack(data[:,233,:],'Sino\sino.tiff',overwrite=True)
        theta = tomopy.angles(data.shape[0], 0, 360)
        tomopy.write_center(data, theta, dpath='theta/Center', mask=True, ratio=.98, filter_name= 'ramlak')
        com = tomopy.find_center(data, theta, tol=0.1)
        a = np.mod(com, 1)
        print(a)
        print(com)


        # recon = tomopy.recon(data, theta, center=503, algorithm='fbp')
        # 424.5
        # recon = tomopy.circ_mask(recon, axis=0, ratio=0.80)
        # options = {'proj_type': 'linear', 'method': 'SIRT', 'num_iter': 80}
        # tomopy.sim.project.add_drift(data, amp=0.2, period=50, mean=1)
        # tomopy.sim.project.fan_to_para(data, 10, 'line')
        options = {'proj_type': 'linear', 'method': 'FBP'}
        recon = tomopy.recon(data, theta, center=com, algorithm=tomopy.astra, options=options, ncore=1, filter_name= 'ramlak')
        recon = tomopy.circ_mask(recon, axis=0, ratio=0.95)
        # plt.imshow(recon[10, :, :])
        # plt.show()

        '''''Save image'''''
        path_save = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save Reconstructed Image')
        print(path_save)
        dxchange.write_tiff_stack(recon, path_save, overwrite=True)

        '''' Save temp'''
        dxchange.write_tiff_stack(recon, path_temp, overwrite=True)


    def Save_button_command(self):
        global proj

    def Citra (self):
        global path_temp

        # Total image
        img_citra = r'C:\Users\Madeena\AppData\Local\Temp_00000.tiff'
        total_citra=int(len(img_citra))
        print('total_citra',total_citra)
        proj = dxchange.read_tiff_stack(img_citra, range(0, total_citra))
        img_citra = proj[0, :, :]
        print(img_citra.shape)
        L_i, P_i = img_citra.shape



        img_view = cv2.resize(img_citra, (int(P_i / 2), int(L_i / 2)), interpolation=cv2.INTER_AREA)
        img_view = Image.fromarray(img_view)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image = img_view

        def Scale(value: None):
            Scale = int(slider.get())
            print(Scale)
            plt.imshow(proj[Scale, :, :])
            img_citra = proj[Scale, :, :]
            L_i, P_i = img_citra.shape
            img_view = Image.fromarray(img)
            img_view = ImageTk.PhotoImage(img_view)
            Label.configure(image=img_view)
            Label.image = img_view

        # Scale
        slider = tk.Scale(root, from_=0, to=total_citra - 1, length=674,
                          resolution=1, orient=tkinter.HORIZONTAL, command=Scale)
        slider.place(x=40, y=617)

    def Sinogram(self):
        #img_sino = cv2.imread(r'C:\Users\Madeena\AppData\Local\'Temp.tiff',0)

        img_sino = cv2.imread(os.path.join(path_save,'Temp_00000.tiff'))

        print(img_sino.shape)
        #L_i, P_i = img_sino.shape
        #size=(int(P_i / 2), int(L_i / 2))

        img_view = cv2.resize(img_sino,(300,300), interpolation=cv2.INTER_AREA)
        img_view = Image.fromarray(img_view)
        img_view = ImageTk.PhotoImage(img_view)
        Label.configure(image=img_view)
        Label.image = img_view



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
