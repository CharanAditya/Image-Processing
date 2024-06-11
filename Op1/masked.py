import cv2 as cv
import numpy as np

img = cv.imread('Images/Dog1.jpg')
cv.imshow('Given Image',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

mask = cv.circle(blank,(img.shape[1]//2 - 106, img.shape[0]//2 - 100),145,255,-1)
cv.imshow('Circle',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

cv.waitKey(0)