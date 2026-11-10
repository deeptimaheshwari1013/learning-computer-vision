import cv2 as cv
import numpy as np
# a pixel is turned off if = 0, on if =1

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30), (370, 370), 255, -1)
# -1 cause we wanna fill the rectangle 

circle = cv.circle(blank.copy(),(200,200),200,255,-1)
# -1 cause we wanna fill the circle

# bitwise AND 
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise AND', bitwise_and)
# it took the 2 images and placed them on top of each other and returned the intersection 

# bitwise OR
# returns the intersecting as well as the non intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise OR',bitwise_or)
# basically u can put them together and find the resulting shape


# bitwise XOR
# good for returning the non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise XOR', bitwise_xor)

# bitwise NOT 
# inverts the binary color 
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise(rectangle) NOT',bitwise_not )


cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)
 





cv.waitKey(0)
