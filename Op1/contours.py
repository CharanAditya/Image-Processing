import cv2 as cv
import numpy as np

img = cv.imread('Images/Dog2.jpg')
cv.imshow('Given Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale Image',gray)

canny_img = cv.Canny(img,125,175)
cv.imshow('Canny Image',canny_img)



cv.waitKey(5000)