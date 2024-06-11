import cv2 as cv
import numpy as np

blank = np.zeros((500,500))
# cv.imshow('Blank',blank)

# Rectangle
rectangle = cv.rectangle(blank.copy(),(100,100),(400,400),255,-1)
cv.imshow('Rectangle',rectangle)

# Circle
circle = cv.circle(blank.copy(),(blank.shape[1]//2 , blank.shape[0]//2),180,255,-1)
cv.imshow('Circle',circle)

'''
Bitwise operations ->

    1. and - bitwise_and
    2. or
    3. xor
    4. not

'''
# Bitwise and - intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise And',bitwise_and)

# Bitwise or - intersecting and non intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise Or',bitwise_or)

# Bitwise XOR - non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)

cv.waitKey(0)