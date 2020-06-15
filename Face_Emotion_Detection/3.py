# -*- coding: utf-8 -*-
"""3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/chethan1996/BEFinalProject/blob/master/Face_Emotion_Detection/3.ipynb
"""

import cv2
import numpy as np
import os 
import time

<<<<<<< HEAD
recognizer = cv2.face.LBPHFaceRecognizer_create()
=======
recognizer = cv2.face_LBPHFaceRecognizer.create()
>>>>>>> 10f4d98fd3c4af48e94b47eddeec84e9d8e806d0
recognizer.read('trainer/trainer.h5')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
eye_detector  = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
nose_detector = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
half_face_detector = cv2.CascadeClassifier('haarcascade_profileface.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

"""## Remember to change the information below!!!"""

#iniciate id counter
id = 1
wait=0
# names related to ids: example ==>chethan: id=1,  etc
names = ['','Chethan']

# Initialize and start realtime video capture
<<<<<<< HEAD
cam = cv2.VideoCapture(-1)
=======
cam = cv2.VideoCapture(0)
>>>>>>> 10f4d98fd3c4af48e94b47eddeec84e9d8e806d0
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        nose = nose_detector.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), 
        int(minH)),)
        eye = eye_detector.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), 
        int(minH)),)
        half_face = half_face_detector.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), 
        int(minH)),)
        
        

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less than 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            if(id=="Chethan"):
                wait+=1
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 
    if(id=="Chethan" and wait>=30):
        wait=0
        print("\nYour a known person so going evaluate your Face Expr")
        cam.release()
        cv2.destroyAllWindows()
<<<<<<< HEAD
        exec(open("/home/chethan/Desktop/test/Emotion-detection/src/get_face_expr.py").read())
=======
        exec(open("get_face_expr.py").read())
>>>>>>> 10f4d98fd3c4af48e94b47eddeec84e9d8e806d0
        
        
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

