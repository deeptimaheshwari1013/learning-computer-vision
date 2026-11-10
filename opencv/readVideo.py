import cv2 as cv

# reading videos 

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'): # if the letter d is pressed then break 
        break
    

capture.release()

cv.destroyAllWindows()

