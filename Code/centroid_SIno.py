import cv2

# input Image
image=cv2.imread('tes.tiff',0)

#diketahui
penjumlahan = 0
sumatas = 0
penjumlahan2 = 0
sumatas2 = 0
hasil=[]

# shape
y, x = image.shape
print(image.shape)

gabung = image[0: y + 0, 0: 1 + 0]

# CenterofMass

for i in range(x-1):
    image1 = image[0: y + 0, x-(x-i): i+1 + 0]
    m,n=image1.shape
    #print('image1=',image1.shape)
    cv2.imwrite('image1.tiff',image1)

    image2 = image[0: y + 0, x-(x-(i+1)): i+2 + 0]
    r, s = image2.shape
    #print('image2=', image2.shape)
    #cv2.imwrite('image2.tiff',image2)

    for z in range(y):
        pixel = image1[z, 0]
        sumatas = (pixel * z) + sumatas
        penjumlahan = penjumlahan + pixel
        #print('z' ,z)
        #print('pixel;',pixel)
    CoM = abs(int(sumatas / penjumlahan))
    hasil.append(int(CoM))
    #print('CoM citra 1: ', CoM)

    for z in range(y):
        pixel2 = image2[z,0 ]
        sumatas2 = (pixel2 * z) + sumatas2
        penjumlahan2 = penjumlahan2 + pixel2
        # print('z' ,z)
    CoM2 = abs(int(sumatas2 / penjumlahan2))
    #print('CoM citra 2: ', CoM2)


    #pergeseran
    pergeseran = abs(int((CoM - CoM2)))
    #print('PERGESERAN',pergeseran)  # dibagi mejadi2
    hitam1 = image2[0: y + 0, 0: n + 0]
    hitam2 = image2[0: pergeseran + 0, 0:s + 0]
    #
    #print('awal:', hitam2.shape)
    hasilimg1 = cv2.vconcat([hitam1, image2])
    hasilimg2 = cv2.vconcat([image2, hitam2])

    # shape1 dengan adanya hitam
    v, _ = hasilimg2.shape

    hasilimg1 = hasilimg1[0:y + 0, 0:n + 0]
    hasilimg2 = hasilimg2[pergeseran:v + 0, 0:s + 0]
    img22 = hasilimg2

    # gabungan
    gabung = cv2.hconcat([gabung, hasilimg2])
cv2.imwrite('gabung.tiff',gabung)
print(hasil)


#
# # pergeseran
# r, t = img2.shape
# hitam2 = img2[0: pergeseran + 0, 0:t + 0]
#
# # print('awal:', hitam.shape)
# img22 = cv2.vconcat([img2, hitam2])
#
# # shape1 dengan adanya hitam
# v, _ = img22.shape
# img22 = img22[pergeseran:r + 0, 0:t + 0]