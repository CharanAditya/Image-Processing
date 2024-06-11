#Essential Functions

import cv2 as cv

img = cv.imread('Images/Dog1.jpg')
cv.imshow('BGR-DOG',img)

#1. Gray scale 
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale-DOG0',gray_img)

#2. Blur the image
blur_img = cv.GaussianBlur(img,(15,15),cv.BORDER_DEFAULT)
cv.imshow('Blurred-DOG',blur_img)

#3. Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow('Edge-cascade',canny)

canny1 = cv.Canny(blur_img,125,175)
cv.imshow('Edge-cascade2',canny1)

#4. Resize image
resized_img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image',resized_img)

#5. Crop image
crooped_img = img[50:500,300:450]
cv.imshow('Cropped Image',crooped_img)


cv.waitKey(0)