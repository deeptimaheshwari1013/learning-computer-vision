import cv2 as cv

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')

cv.imshow('Cat', img)
# a 3 channel BGR image (blue green red)
# converting colored image to grayscale
# see the intensity distribution of pixels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# how to blur an image (removing noise in image)
# using a gaussian blur (uses a bell shaped mathematical formula)
# kernel size : refers to teh dimensions of a small matrix used as a sliding window to perform mathematical operations
# the kernel size has to be an odd number 

blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# creating an edge cascade(finding the edges that are present in the image)
# canny edge detector 
canny = cv.Canny(img, 125,175)
cv.imshow('edges', canny)

# if you pass in the blur, you will reduce the amount of edges found 

# dilating the image (takes the structured element)
#expands the bright(white) regions
# larger kernels produce more expansion
dilated = cv.dilate(canny,(7,7),iterations=1) # kernel size
cv.imshow('dilaed', dilated)

# eroding (shrinks the bright regions)
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('eroded', eroded)

# resizing an image 
# interpolation is useful if u r shrinking the image (INTER_AREA)
# but if u r tryign to enlarge the image to a much larger dimension, use INTER_LINEAR / INTER_CUBIC
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)


#cropping an image
# uses the fact that images are arrays, we can use array slicing. (select a portion of the image on the basis of ur pixel values)

cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)