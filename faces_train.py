import os
import cv2 as cv
import numpy as np 

people = []
for i in os.listdir('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/train') :
    people.append(i)
    
DIR = '/Users/vishwanathmaheshwary/opencv/learning-computer-vision/opencv/Photos/train'
features = []
labels = []

haar_cascade = cv.CascadeClassifier('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/haar_face.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect :
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
            
            
create_train()
print('Training done!!')

features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'length of the features = {len(features)}')
print(f'length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and the labels list 
face_recognizer.train(features,labels)

face_recognizer.save('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/face_trained.yml')

np.save('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/features.npy', features)
np.save('/Users/vishwanathmaheshwary/opencv/learning-computer-vision/labels.npy', labels)


