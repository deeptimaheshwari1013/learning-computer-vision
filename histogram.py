import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/cat.jpg')
cv.imshow('og img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)



# histograms basically allow u to visualize the distribution of pixel intensties in an img
# intution of pixel distribution in the img

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

mask= cv.bitwise_and(gray,gray,mask=circle)

# grayscale histogram 
gray_hist = cv.calcHist([gray],[0], mask,[256], [0,256])

cv.imshow('masked img', mask)
# no. of channels (specify the channel we want to compute a histogram)
# provide a mask - do we want to compute a histogram for a specific portion of the img?
# histSize = no. of bins that we want to use for computing the histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# the no. of bins across the x axis - the intervals of pixel intensities

# color histograms
maskC = cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked color img', maskC)



plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
    
plt.show()

cv.waitKey(0)
