import cv2 as cv
import matplotlib.pyplot as plt

'''
OpenCV assumes that the given image is in BGR format
Matplotlib assumes that the given image is in RGB format
RGB = inverse of (BGR)
- You can convert in the reverse formats too
- You cannot directly convert from gray to HSV
'''

img = cv.imread('Images/Dog2.jpg')
cv.imshow('Given Image' , img)

# plt.imshow(img)
# plt.show()


#Gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale',gray)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV version',hsv)

#BRG to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB Version',lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('In RGB format' , rgb)
cv.waitKey(0)