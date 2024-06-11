import cv2 as cv

#Introduction to images
"""
img  = cv.imread("Images/Dog1.jpg")
cv.imshow("Image of Dog-1",img)
cv.waitKey(0)
"""

# Height : shape[0]
# Width : shape[1]

def rescaleFrame(frame , scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame , dimensions,interpolation=cv.INTER_AREA)

img = cv.imread("Images/Dog1.jpg")
cv.imshow("Image of Dog-1" ,img)
cv.imshow("Image of Dog-1",rescaleFrame(img))

cv.waitKey(0)