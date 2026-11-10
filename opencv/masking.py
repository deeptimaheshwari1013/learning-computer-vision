import cv2 as cv
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 -5), 100, 255, -1)
cv.imshow('Mask',mask)
# the mask has to have the same dimension as the image

# masking essentially allows us to focus on certain parts of an img

masked = cv.bitwise_and(img,img, mask= mask)
cv.imshow('Masked img', masked)


# you can make diff shapes by performing bitwise operations on rectangles and circles and use those
# shapes as masks for ur imgs (i havent tried that but its quite simple)

# just make sure the dimensions of mask is same as that of the img



cv.waitKey(0)
