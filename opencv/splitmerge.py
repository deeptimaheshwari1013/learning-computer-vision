import cv2 as cv
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og image',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

#opencv allows u to split an image into its color channels
b,g,r = cv.split(img)

blueR = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank, blank,r])

# color coding the specific color channels 
cv.imshow("Blue channel",blueR)
cv.imshow("Green channel",green)
cv.imshow("red channel", red)



cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("red", r)
# depicted as grayscale imgs that show the distribution of pixel intenstities
# the regions that are whiter show more of that color

# grayscale images have a shape of one

print(img.shape) # prints an extra '3' element showing the color channels
print(b.shape)
print(g.shape)
print(r.shape)

# merge the channels together 
merged = cv.merge([g,b,r])
cv.imshow("merged img", merged)



cv.waitKey(0)
