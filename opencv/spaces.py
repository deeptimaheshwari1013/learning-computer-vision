import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og image', img)

# color spaces : HSV, RGB, grayscale 

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray)

# grayscale images basically show u the distribution of pixel intensity 

# BGR to HSV (Hue-saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv image',hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("l*a*b",lab)
 
#opencv read images in a BGR format 
# outside of opencv we use the RGB format 



#plt.imshow(img)
#plt.show()

# matplot lib has no idea that this image is a BGR image and displays it as it were an an RGB image
# so thats why u see an inversion of colors 


#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb img',rgb)

# u can do viceversa conversion to like hsv to bgr, lab to bgr but u cant do grayscale to hsv directly, it would have 
# to go through the bgr conversion first to be converted into a hsv img 

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv-->bgr", hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab-->bgr",lab_bgr)

cv.waitKey(0)
