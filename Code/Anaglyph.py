import os
import tkinter
from tkinter import filedialog
from PIL import Image
import tempfile
from PIL import ImageTk
import cv2
import imutils
import numpy as np
import PIL, PIL.Image, PIL.ImageOps, PIL.ImageEnhance

path = tempfile.gettempdir()

def imgR():
    path_image = filedialog.\
        askopenfilename(initialdir="/", title="select file",
        filetypes=(
            ("Image", "*.tiff"), ("Image", "*.tif"),
            ('Image', "*.bmp"), ("Image", "*.jpg"),
            ("Image", "*.png"), ("Image", "*.txt")
        ))
    print(path_image)

    global imgR
    imgR=cv2.imread(path_image)
    cv2.imwrite(os.path.join(path, 'imgR.tiff'), imgR)
    imgR=PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff',mode='r').convert('RGB')
    imgR = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgR.tiff', mode='r').convert('L')

def imgL():
    path_image = filedialog. \
        askopenfilename(initialdir="/", title="select file",
        filetypes=(
            ("Image", "*.tiff"), ("Image", "*.tif"),
            ('Image', "*.bmp"), ("Image", "*.jpg"),
            ("Image", "*.png"), ("Image", "*.txt")
        ))
    print(path_image)

    global imgL
    imgL = cv2.imread(path_image)
    cv2.imwrite(os.path.join(path, 'imgL.tiff'), imgL)
    imgL=PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff',mode='r').convert('RGB')
    imgL = PIL.Image.open(r'C:\Users\Madeena\AppData\Local\Temp\imgL.tiff', mode='r').convert('L')




def fil():
    global imgR,imgL
    if selected.get()==1:
        # color filtering
        red_img=PIL.ImageOps.colorize(imgL,(0,0,0),(255,0,0))
        cyan_img=PIL.ImageOps.colorize(imgR,(0,0,0),(0,255,255))

        # red_img = np.array([255,0,0])
        # cyan_img = np.array([0,255,255])




        blend=PIL.Image.blend(red_img,cyan_img,0.5)
        #blend=cv2. addWeighted(red_img,0.5,cyan_img,0.5)
        np_blend=np.array(blend)
        im_comb= imutils.resize(np_blend,height=600)

        im_comb=cv2.cvtColor(im_comb,cv2.COLOR_BGR2RGB)

        numpy_hor=np.concatenate((red_img,cyan_img),axis=1)
        numpy_hor=cv2.cvtColor(numpy_hor,cv2.COLOR_BGR2RGB)
        cv2.imwrite('Red an Cyan.tiff', cv2.resize(numpy_hor,(0,0), None,.7,.7))
        red_cyan=Image.open('Red an Cyan.tiff')
        red_cyan.show()

        cv2.imwrite('Anaglyph.tiff', im_comb)
        result = Image.open('Anaglyph.tiff')
        result.show()

#Display
root=tkinter.Tk()

selected=tkinter.IntVar()
rad1= tkinter.Radiobutton(root, text='Anaglyph', width=50, value=1,
                          variable=selected, command=fil)
rad1.grid(column=0, row=4)

#button
btn=tkinter.Button(root, text='ImgL', width=50,
                   command=imgL)
btn.grid(column=0, row=0, padx=5, pady=5)
btn2=tkinter.Button(root, text='ImgR', width=50,
                   command=imgR)
btn2.grid(column=0, row=1, padx=5, pady=5)
root.mainloop()



