import cv2 as cv

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og image',img)

# thresholding : binary realisation of an image
# take an image and convert it to a binary img where pixels are 0(black) / 255(white)
# take an img and a "thresholding" value
# and compare each pixel of the img to the threshold value 
# if the pixel intensity is less than the threshold value -> set the pixel intensity =0 
# if its above, we set it to 255(white)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# simple thresholding
# takes in the grayscale img
threshold, thresh = cv.threshold(gray,160,255,cv.THRESH_BINARY)
# thresh is the binarized(or thresholded) img 
# threshold = 150 (the threshold value will be returned)
# if val>= 255 -->1 o/w it sets it to 0 

cv.imshow('simple thresholded', thresh)

# inverse thresholded img 
threshold, thresh_inverse = cv.threshold(gray,160,255,cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse', thresh_inverse)

# adaptive thresholding
# the down side to simple thresholding is manually specify the value 
#let the computer find the optimal threshold value and then it binarizes the img

# adaptive method tells machine which method to use when computing when optimal threhsolded value
adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,
                                      3 )
cv.imshow('adaptive thresholding', adaptive_thresh)

# the block size: essentially the neighborhood size of the kernel size
#cvalue: an int that is subracted from the mean allowing us to fine tune our threshold

# we've defined a kernel size/ window that is drawin of this img
# opencv computes a mean over these neighbourhood pixels and find the optimal threshold value for that specific part

# the more u subract from the mean, the more accurate it is
# calculated the optimal thresholded value on the basis of the mean
# ADAPTIVE_THRESH_GAUSSIAN --> add a weight to each pixel value, and compute the mean across it


cv.waitKey(0)