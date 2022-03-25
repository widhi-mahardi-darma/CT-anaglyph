import cv2
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np

# input Image
image=cv2.imread('baru.tiff',0)

# diketahui
nilai_CoM=[]
nilai_poli=[]
nilai_pengurangan=[]
nilai_koreksi=[]

# shape
y_image, x_image = image.shape
print(image.shape)

# image1 = image[0: y_image + 0, int(x_image/2): int(x_image/2)+1 + 0]
#
# mid_y, l= ndi.center_of_mass(image1)
# print('nilai tengah', mid_y)

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
    print(cy)

mid_y=nilai_CoM[int(x_image/2)]
print('nilai tengah', mid_y)
# Print nilai polinomial
for z in range (x_image-1):

    pengurangan=((nilai_CoM[z])-(int(mid_y)))
    nilai_pengurangan.append(pengurangan)
    print(pengurangan)

    # TODO: CoM dikurangi dengan selisih
    result1= ((nilai_CoM[z])-(pengurangan))
    nilai_koreksi.append(result1)

# TODO: Hasil
pengurangan=np.array((nilai_pengurangan))

#y= np.array(nilai_koreksi)
x = np.arange(0.0, x_image-1, 1.0)
plt.plot(x,pengurangan)
#plt.plot(x,y)
plt.grid()
plt.show()



for i in range(x_image-1):
    #image 1
    image1 = image[0: y_image + 0, x_image-(x_image-i): i+1 + 0]

    m,n=image1.shape
    cv2.imwrite('image1.tiff',image1)

    # image 1
    img = cv2.imread('image1.tiff')
    img = img.mean(axis=-1)  # in grayscale

    #image 2
    image2 = image[0: y_image + 0, x_image - (x_image - (i + 1)): i + 2 + 0]
    r, s = image2.shape
    cv2.imwrite('image2.tiff',image2)

    # image 2
    img2 = cv2.imread('image2.tiff')
    img2 = img2.mean(axis=-1).astype('int')  # in grayscale

    pergeseran=int(nilai_pengurangan[i])
    print(pergeseran)

    if pergeseran <=-1:
        pergeseran = abs(pergeseran)
        #print('kurang')
        # print('PERGESERAN',pergeseran)  # dibagi mejadi2
        hitam1 = image2[0: y_image + 0, 0: n + 0] #n=1
        hitam2 = image2[0: pergeseran + 0, 0:s + 0] #s=1
        #
        # print('awal:', hitam2.shape)
        hasilimg1 = cv2.vconcat([image2, hitam1])
        hasilimg2 = cv2.vconcat([hitam2, image2])

        # shape1 dengan adanya hitam
        v, _ = hasilimg2.shape

        hasilimg1 = hasilimg1[0:y_image + 0, 0:n + 0]
        hasilimg2 = hasilimg2[pergeseran:v + 0, 0:s + 0]
        img22 = hasilimg2

        gabung = cv2.hconcat([gabung, hasilimg2])

    else:
        #print('lebih')
        # print('PERGESERAN',pergeseran)  # dibagi mejadi2
        hitam1 = image2[0: y_image + 0, 0: n + 0]
        hitam2 = image2[0: pergeseran + 0, 0:s + 0]
        #
        # print('awal:', hitam2.shape)
        hasilimg1 = cv2.vconcat([hitam1, image2])
        hasilimg2 = cv2.vconcat([image2, hitam2])

        # shape1 dengan adanya hitam
        v, _ = hasilimg2.shape

        hasilimg1 = hasilimg1[0:y_image + 0, 0:n + 0]
        hasilimg2 = hasilimg2[pergeseran:v + 0, 0:s + 0]
        img22 = hasilimg2
        # gabungan
        gabung = cv2.hconcat([gabung, hasilimg2])


cv2.imwrite('gabung_tes.tiff', gabung)