import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#1.Colour the entire screen
blank[200:300,300:400] = (0,255,255)
cv.imshow('Blank',blank)

#2.Draw a Rectangle
cv.rectangle(blank,(10,10),(250,250),(200,200,200),thickness=cv.FILLED)
cv.imshow('Blank',blank)

#3.Draw a circle
cv.circle(blank,(430,430),40,(120,130,250),thickness=4)
cv.imshow('Blank',blank)

#4.Draw a line
cv.line(blank,(0,0),(blank.shape[0]//3 , blank.shape[1]//2),(255,255,255),10)
cv.imshow('Blank',blank)

#5.Write text on the image
cv.putText(blank,'HELLO',(255,255),cv.FONT_HERSHEY_TRIPLEXk,1,(255,10,255))
cv.imshow('Blank',blank)

cv.waitKey(0)