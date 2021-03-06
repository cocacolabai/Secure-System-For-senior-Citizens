# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/chethan1996/BEFinalProject/blob/master/Face_Emotion_Detection/2.ipynb
"""

import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
eye_detector  = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
nose_detector = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
half_face_detector = cv2.CascadeClassifier('haarcascade_profileface.xml')

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = face_detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            eye = eye_detector.detectMultiScale(img_numpy)
            nose = nose_detector.detectMultiScale(img_numpy)
            half_face = half_face_detector.detectMultiScale(img_numpy)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.h5') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} Faces Trained. Exiting Program".format(len(np.unique(ids))))
print("\n Know your a known persons list ):-")

