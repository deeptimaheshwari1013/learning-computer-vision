import cv2 as cv
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# contours are basically the boundaries of the object. the lines or curves that join the continous points along the boundary 

#converting the image into grey scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 125,175)

# RETR_TREE -> for hierarchial contours 
# RETR_LIST -> if u want all the contours in the image 
# RETR_EXT -->only the external contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# the findContours method looks at the structuring element 
# hierachrchies refers to the hierarchial representation of the contours
# contours is a list

print(len(contours))

# the number of contours will be reduced by blurring the image 

# threshold - looks at an image and tries to binarize that by comparing each pixel's instensity to a threshold value
# thresholding makes it easier to identify objects

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# drawing the contours in the blank image 
cv.drawContours(blank, contours, -1,(0,0,255), 2)
cv.imshow('contours drawn', blank)

cv.waitKey(0)