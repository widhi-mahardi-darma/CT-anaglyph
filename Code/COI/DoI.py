import tkinter
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
import math


# Layout
width  = 770
height = 1260
display= tkinter.Tk()
display.minsize(width=width, height=height)
display.resizable(True,True)

# input Image
image=cv2.imread('sino_industri.tiff',0)


# deteksi tepi

# Canny Edge Detection
edges = cv2.Canny(image=image, threshold1=100, threshold2=200)
cv2.imwrite('edge.tiff',edges)

plt.subplot(2,2,1),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges,cmap = 'gray')
plt.title('Edge'), plt.xticks([]), plt.yticks([])

plt.show()

# diketahui
nilai_CoM=[]
nilai_poli=[]
nilai_pengurangan=[]
nilai_koreksi=[]
Y=[]

# shape
y_image, x_image = image.shape
print(image.shape)

# CenterofMass
gabung = image[0: y_image + 0, 0: 1 + 0]

for i in range(x_image-1):
    #image 1
    image1 = image[0: y_image + 0, x_image-(x_image-i): i+1 + 0]

    m,n=image1.shape
    cv2.imwrite('image1.tiff',image1)

    #image 1
    img = cv2.imread('image1.tiff')

    cy, cx,_= ndi.center_of_mass(img)
    nilai_CoM.append(int(cy))

#Grafik
print(nilai_CoM)
y= np.array(nilai_CoM)
print(y)
x = np.arange(0.0, x_image-1, 1.0)

#polynomial
z=np.polyfit(x, y, 5)
model4 = (np.poly1d(np.polyfit(x, y, 5)))

#define scatterplot
polyline = np.linspace(0, x_image-1, 50)

#Input data Fitting
Amplitudo =75 #Amplitudo
Frekuensi= 0.021
Phase=-2.7
Constanta=624

for i in range (x_image-1):
    Sin=math.sin(Frekuensi*i+Phase)
    fitting=Amplitudo*Sin+Constanta
    Y.append(fitting)
Y=np.array(Y)

plt.plot(x,y) # biru
plt.plot(x, Y, '--', color='red')
#plt.title("y=%.4fx^5+%.4fx^4+%.4fx^3+%.4fx^2+%.4fx+%.4f"%(model4[5],model4[4],model4[3],model4[2],model4[1],model4[0]))
plt.grid()
plt.show()

frame= 300
rad= Frekuensi*frame
derajat= 180*rad/math.pi
print('derajat', derajat)


# Layout
display.title("DoI")
display.mainloop()