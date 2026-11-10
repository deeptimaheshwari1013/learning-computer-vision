import cv2 as cv
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og image',img)

# from a programming perspective u can think of gradients as edges

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# computes the gradients of this grayscale imng
# white to black, considered a postive and a negative slope

# sabel gradient magnitude method
# sobel computes the gradients in 2 directions, x and y 
# CV_64F - is the depth of the gradient
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)


# combing both the sobel gradients
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined sobel', combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('Canny', canny)
# canny(multi stage process) actually uses sobel in one of its stages


cv.waitKey(0)
