import cv2

# input Image
image=cv2.imread('baru.tiff',0)

#diketahui
penjumlahan = 0
sumatas = 0
penjumlahan2 = 0
sumatas2 = 0

# shape
y, x = image.shape
print(image.shape)

gabung = image[0: y + 0, 0: 1 + 0]

# CenterofMass

#koordinat tengah
tengah=int(x/2)
for u in range(y):
    image_tengah = image[0: y + 0, tengah: tengah + 1 + 0]
    m, n = image_tengah.shape
    pixel_tengah = image_tengah[u, 0]
    if pixel_tengah >=1:
        roi_tengah=u
        break

print('berapa roi tengah', roi_tengah)

for i in range(x-1):
    image1 = image[0: y + 0, x-(x-i): i+1 + 0]
    m,n=image1.shape
    #print('image1=',image1.shape)
    #cv2.imwrite('image1.tiff',image1)
    image2 = image[0: y + 0, x - (x - (i + 1)): i + 2 + 0]
    r, s = image2.shape


    for z in range(y):
        pixel = image2[z, 0]
        if pixel >=1:
            roi_image=z
            break
    #print('roi_image',roi_image)


    #pergeseran
    pergeseran = (int((roi_tengah - roi_image)))


    print('PERGESERAN',pergeseran)  # dibagi mejadi2
    #if pergeseran <= 0:
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

