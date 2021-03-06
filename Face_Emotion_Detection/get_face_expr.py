# -*- coding: utf-8 -*-
"""Get_Face_Expr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/chethan1996/BEFinalProject/blob/master/Face_Emotion_Detection/Get_Face_Expr.ipynb
"""



import numpy as np
import argparse
import cv2
import imutils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
import os
import threading
from twilio.rest import Client #Call API
#importing SMTP Library
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

base_path="/home/chethan/Desktop/test/Emotion-detection/src/data/face-expression-recognition-dataset/images/images/"


def get_contacts(filename):
            """
            Return two lists names, emails containing names and email addresses
            read from a file specified by filename.
            """

            names = []
            emails = []
            with open(filename, mode='r', encoding='utf-8') as contacts_file:
                for a_contact in contacts_file:
                    names.append(a_contact.split()[0])
                    emails.append(a_contact.split()[1])
            return names, emails

def read_template(filename):
            """
            Returns a Template object comprising the contents of the 
            file specified by filename.
            """

            with open(filename, 'r', encoding='utf-8') as template_file:
                template_file_content = template_file.read()
            return Template(template_file_content)

def main():

            MY_ADDRESS = 'securesystem57@gmail.com'
            PASSWORD = 'securesystem2020'
            names, emails = get_contacts('/home/chethan/Desktop/test/Emotion-detection/src/contacts.txt') # read contacts
            message_template = read_template('/home/chethan/Desktop/test/Emotion-detection/src/msg.txt')
            MY_ADDRESS = os.environ['EMAIL']
            PASSWORD = os.environ['EMAIL_PWD']
            names, emails = get_contacts('contacts.txt') # read contacts
            message_template = read_template('msg.txt')

            # set up the SMTP server
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(MY_ADDRESS, PASSWORD)

            # For each contact, send the email:
            for name, email in zip(names, emails):
                msg = MIMEMultipart()       # create a message

                # add in the actual person name to the message template
                message = message_template.substitute(PERSON_NAME=name.title())

                # Prints out the message body for our sake
                print(message)

                # setup the parameters of the message
                msg['From']=MY_ADDRESS
                msg['To']=email
                msg['Subject']="Secure System Notification"

                # add in the message body
                msg.attach(MIMEText(message, 'plain'))

                # send the message via the server set up earlier.
                s.send_message(msg)
                del msg

            # Terminate the SMTP session and close the connection
            s.quit()

def send_mail():

        if __name__ == '__main__':
            main()

# Define data generators
train_dir = base_path+'train'


def send_mail():
      if __name__ == '__main__':
               main()

def make_phone_call():
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml='<Response><Say>please take care of Your parents they seems SAD today</Say></Response>',
                            to=os.environ['MY_NUMBER'],
                            from_='+19094559497'
                        )

    print("call connceted succfully")
    print(call.sid)
    
# Define data generators
"""train_dir = base_path+'train'
val_dir = base_path+'validation'

num_train = len(train_dir)
num_val = len(val_dir)
batch_size = 64
num_epoch = 50

train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
<<<<<<< HEAD
        class_mode='categorical')
=======
        class_mode='categorical')"""

# Create the model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

model.load_weights('/home/chethan/Desktop/test/Emotion-detection/src/data/Model_Save/model.h5')
model.load_weights('Model_Save/model.h5')

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
count_sad=0
# start the webcam feed
cap = cv2.VideoCapture(-1)
while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=720)
    if not ret:
        break
    facecasc = cv2.CascadeClassifier('/home/chethan/Desktop/test/Emotion-detection/src/haarcascade_frontalface_default.xml')

    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        #vgg_result=return_prediction(cropped_img)
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        #print(emotion_dict[maxindex])
        if (emotion_dict[maxindex]=="Sad"):
            count_sad+=1
            #print(count_sad)
                
        cv2.putText(frame, emotion_dict[maxindex], (x+10, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Video', cv2.resize(frame,(720,620),interpolation = cv2.INTER_CUBIC))
    if(count_sad>=5):
        send_mail()
        print("Mail Sent successfully")

   
    if(count_sad>=5 and count_sad < 10):
        mail_thread=threading.Thread(target=send_mail)
        mail_thread.start()
        print("Mail Sent successfully")
    if(count_sad>=30): #if Sadness continue then call to care taker
        call_thread=threading.Thread(target=make_phone_call)
        call_thread.start()
        count_sad=0 #intialize to zero after notify

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

