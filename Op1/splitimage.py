import cv2 as cv
import numpy as np

img = cv.imread('Images/Dog1.jpg')
cv.imshow('Given image',img)

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

'''
Output ->

(510, 900, 3)
(510, 900)
(510, 900)
(510, 900)
'''

# Merge the colour channels
merged = cv.merge([b,g,r])
cv.imshow('Merged image ',merged)

# Displaying with respect to the colours
blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue only ',blue)
cv.imshow('Green only',green)
cv.imshow('Red only',red)


cv.waitKey(0)
print("Blue ->")
print(blue[0][0])
print("Blue 1->")
print(b[0][0])