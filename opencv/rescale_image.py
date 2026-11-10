import cv2 as cv
# takes a frame and rescales the frame by a particular value
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale )# frame.shape[1] --> width of the pic
    height = int(frame.shape[0] * scale )# frame.shape[0] --> height of the pic
    dimensions = (width,height)
    
    
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA )




img = cv.imread('opencv/Photos/cat.jpg')
cv.imshow('Cat',img)

cv.imshow('cat_resized', rescaleFrame(img,scale=0.5))

cv.waitKey(0)
