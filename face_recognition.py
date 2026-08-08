import numpy as np 
import cv2 as cv

haar_cascade = cv.CascadeClassifier('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/haar_face.xml')


people = ['Ben Affleck', 'Elton John','Jerry Seinfield', 'Madonna', 'Mindy Kaling']
#features = np.load('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/features.npy', allow_pickle= True)
#labels = np.load('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/face_trained.yml')

img = cv.imread('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/val/ben_afflek/3.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

#detect the face in the img 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img,str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0,255,0), thickness=2)
    
    cv.rectangle(img,(x,y),(x+w,y+h), color=(0,255,0), thickness=2)

cv.imshow('detected face', img)
cv.waitKey(0)

#opencv recognizer is not the best, 