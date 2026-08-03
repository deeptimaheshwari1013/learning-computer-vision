import cv2 as cv
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')

cv.imshow('og img', img)

#Translation (shifting the image)
# x -> no. of pixels u wanna shift on the x axis
#y -> no. of pixels u wanna shift on the y axis
def translate(img, x,y):
    # this is the translation matrix
    transMat  = np.float32([[1,0,x], [0,1,y]])
    # dimensions of the image(width,height)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

    # x<0 --> translate the image to the left 
    # y<0--> translate the image up 
    # x>0 --> shifting it right
    # y>0 --> shifting it down
    
translated = translate(img,100,80)
cv.imshow('translated img', translated)

# rotation 
# opencv allows u to specify any rotation point that u wanna rotate around 
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width/2, height/2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (height, width)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('rotated', rotated)

# inter_cubic is slower but of better quality


#flipping 
flip = cv.flip(img, 0)
# 0 --> flipping the image vertically (over the x axis)
# 1 --> flipping the image horizontally (over the y axis)
# -1 --> flipping both vertically and horizontally
cv.imshow('flipped', flip)

cv.waitKey(0)