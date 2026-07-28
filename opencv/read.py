import cv2 as cv

# reading images 

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0);

