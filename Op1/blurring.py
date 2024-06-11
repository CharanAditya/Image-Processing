import cv2 as cv

img = cv.imread('Images/Dog1.jpg')
cv.imshow('Given image',img)

#1. Average blur
average = cv.blur(img,(11,11))
cv.imshow('Average Blur',average)

#2. Gaussian blur
gauss = cv.GaussianBlur(img,(11,11),0)
cv.imshow('Gaussian Blur',gauss)

#3. Median blur
med = cv.medianBlur(img,11)
cv.imshow('Median Blur',med)

#4. Bilateral blurring
bil = cv.bilateralFilter(img,10,35,30)
cv.imshow('Bilateral blurring',bil)

cv.waitKey(0)