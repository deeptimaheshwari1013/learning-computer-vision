import cv2 as cv

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og img', img)

# we generally tend to smooth the image when it has a lot of noise 
# smooth out the img = reduce some of the noise 
# kernel/window, the window has a size --> kernel size (no.of rows, no. of columns)
#blur is applied to the middle pixel as a result to the pixels around it(surrounding pixels)

# averaging 
# we define a kernel window over a specific portion of an img 
# the window will compute the pixel intensity of the middle pixel of the true center 
# the window keeps on sliding to the entire pic 

average = cv.blur(img, (5,5))
cv.imshow('average blur', average)
# the higher kernel size u specify is the more blur u get in the image


# gaussian blur 
# instead of calculating the average of the surrounding pixels, each running pixels is given a particular weight
# the avg of the product of those weights give u the value for the true center
# the gaussian blur is more natural as compared to averagign 

gauss = cv.GaussianBlur(img,(5,5),0)
cv.imshow('gaussian blur',  gauss)
# a certain weight value was added when computing the blur 


# median blur 
# finds the median of the surrounding pixels
# more effective in reducing noise in an img as comapred to avg.
# good at removing salt and pepper noise 
median = cv.medianBlur(img,5) # opencv automatically assumes the tuple size will be 3 x 3
cv.imshow('median image', median)
# median blur is not meant for a high kernel size (<5)

# bilateral blurring 
# most effective, applies blurring but retains the edges in the img 
# sigma color and sigma space!! 
# larger values of space sigma means that pixels further out from the central pixel will influence the blurring
# u dont have kernel size, u have diameter
bilateral = cv.bilateralFilter(img, 5, 35,45) 
cv.imshow('bilateral img', bilateral)

cv.waitKey(0)
