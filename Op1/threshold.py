import cv2 as cv

img = cv.imread('Images/Dog1.jpg')
cv.imshow('Given image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale',gray)

'''
The threshold function returns two values
    - threshold -> the threshold value we specify
    - thresh -> the image after carrying out the necessary conversions
'''
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Binary',thresh)

cv.waitKey(0)