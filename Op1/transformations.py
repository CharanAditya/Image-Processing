import cv2 as cv
import numpy as np

img = cv.imread('Images/Dog2.jpg')
cv.imshow('Given image',img)

#1. Translation of image

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
cv.imshow('Translated image',translated)

#2. Rotation

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2 , height//2)
    #rotMatrix = cv.getRotationMatrix2D(rotPoint,angle,scaleFactor)
    rotMatrix = cv.getRotationMatrix2D(rotPoint , angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMatrix,dimensions)
rotated = rotate(img,0)
cv.imshow('Rotated image',rotated)

#3. Resizing

#4. Flipping
"""
    1 -> Horizontally, over the y-axis
    0 -> Vertically over the x-axis
    -1 -> Over both, vertically and horizontally
"""

flipped_img = cv.flip(img,1)
cv.imshow('Flipped image',flipped_img)


cv.waitKey(0)

