masked = cv.bitwise_and(img , img , mask=circle)
cv.imshow('Masked',masked)