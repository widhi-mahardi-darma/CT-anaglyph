import matplotlib.image as mpimg
import scipy.ndimage as ndi
import tkinter as tk
import cv2
import tempfile
import os
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np



display= tk.Tk()
# Upload Image
path_image = filedialog. \
    askopenfilename(multiple=True, initialdir="/", title="Image Left",
                    filetypes=(
                        ("Image", "*.tiff"), ("Image", "*.tif"),
                        ('Image', "*.bmp"), ("Image", "*.jpg"),
                        ("Image", "*.png"), ("Image", "*.txt")
                    ))



# split image
var = display.tk.splitlist(path_image)
image = []

# jumlah banyak citra
global jumlah_img
jumlah_img = len(var)
print("jumlah image:", jumlah_img)

for f in var:
    a = cv2.imread(f)
    image.append(a)

path = tempfile.gettempdir()
hasil_x=[]

for i in range(jumlah_img):
    cv2.imwrite(os.path.join(path, 'img_com.tiff'), image[i])
    img=cv2.imread(os.path.join(path, 'img_com.tiff'))

    img = img.mean(axis=-1).astype('int')  # in grayscale

    cy, cx = ndi.center_of_mass(img)
    print('Hasil y =',int(cy))
    print('Hasil X=', int(cx))
    hasil_x.append(int(cx))



# Plot
y=np.array([hasil_x])
x=np.array([i*1 for i in range(jumlah_img)])

y1=np.array([1,2,3,4,5,6,6])
x1 = np.arange(0.0, jumlah_img, 1.0)
print(hasil_x)
print(y1)

# plt.figure()
# plt.subplot(221)
plt.scatter(x1,y)
plt.ylabel('CoM')


plt.show()



