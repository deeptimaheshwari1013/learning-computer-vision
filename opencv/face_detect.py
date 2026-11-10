import cv2 as cv

# convert the img into a grayscale img
# these haarcascahes looks at an object in an img and using the edges tires to determine whether its a face or not 
img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/lady.jpg')
cv.imshow('person',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# reading the haarcascade file 
haar_cascade = cv.CascadeClassifier('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/haar_face.xml')
# this method will read in those lines of XML code and store that in a variable called haar_cascade

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)
# returns the rectangular coordinates of that face as a list to faces_rect 

print(f'number of faces found = {len(faces_rect)}')

# we can actually loop over this list and essentially grab the coordinates of those imgs 
# and draw a rectangle over the detected faces

for (x,y,w,h) in faces_rect : 
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0), thickness=3)

cv.imshow('Detected img', img)

#haarcascades are really sensitive to noise in an img
# by increasing the min_neighbours parameter, u can decrease the sensitivity

# u can kind loop through the value of minNeighbours abd tweak the vales and get a good answer
# u can extend this to videos too (detect haarcascades in each individual frame)
 



cv.waitKey(0)
