import cv2 as cv
import numpy as np 


blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)


# paint the image s certain color 
blank[200:300 , 300:400] = 255,255,0
cv.imshow('Green', blank)

# draw a rectangle 
cv.rectangle(blank, (0,0),(250,250), (0,255,0), thickness = 2)
# cv.FILLED or -1 -> fills in the rectangle (pass this in thickness params)


cv.imshow('rectangle',blank)


# draw a circle 
cv.circle(blank,(250,250),40, (0,0,255), thickness = -1)
cv.imshow("circle", blank)

# draw a line 
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=4)
cv.imshow("line", blank)

# write text on the image 
cv.putText(blank,'Hello there, Im deepti', (225,225),cv.FONT_HERSHEY_DUPLEX, 1.0,(255,255,255),2)
cv.imshow("text", blank)

cv.waitKey(0)
