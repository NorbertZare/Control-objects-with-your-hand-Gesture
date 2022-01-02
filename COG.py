import cv2 
import mediapipe as mp
from math import hypot
import numpy as np 
import serial
import time

share_x,share_y=20,10
edit_x,edit_y=235,10
delete_x,delete_y=450,10

wb,hb=150,70

cap = cv2.VideoCapture(0)



mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
spo=30

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #Share
    cv2.rectangle(img, (share_x,share_y), (share_x+wb,share_y+hb), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, "Share", (share_x+5,share_y+50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)
    #Edit
    cv2.rectangle(img, (edit_x,edit_y), (edit_x+wb,edit_y+hb), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, "Edit", (edit_x+25,edit_y+50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)
    #Delete
    cv2.rectangle(img, (delete_x,delete_y), (delete_x+wb,delete_y+hb), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, "Delete", (delete_x,delete_y+50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)


    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy]) 
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    
    if lmList != []:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]


        cv2.circle(img,(x2,y2),6,(255,0,0),cv2.FILLED)


        if share_x < x2 < share_x+wb and share_y < y2 < share_y+hb:
            # Share
            cv2.rectangle(img, (share_x, share_y), (share_x + wb, share_y + hb), (0, 255, 100), cv2.FILLED)
            cv2.putText(img, "Share", (share_x + 5, share_y + 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)
            ca = 200
            ca = str(ca)
            arduino.write(bytes(ca, 'utf-8'))


        if edit_x < x2 < edit_x+wb and edit_y < y2 < edit_y+hb:
            # edit
            cv2.rectangle(img, (edit_x, edit_y), (edit_x + wb, edit_y + hb), (0, 255, 100), cv2.FILLED)
            cv2.putText(img, "Edit", (edit_x + 25, edit_y + 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)
            ca = 300
            ca = str(ca)
            arduino.write(bytes(ca, 'utf-8'))

        if delete_x < x2 < delete_x+wb and delete_y < y2 < delete_y+hb:
            # delete
            cv2.rectangle(img, (delete_x, delete_y), (delete_x + wb, delete_y + hb), (0, 255, 100), cv2.FILLED)
            cv2.putText(img, "Delete", (delete_x , delete_y + 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 6)
            ca = 400
            ca = str(ca)
            arduino.write(bytes(ca, 'utf-8'))

        sp = hypot(x2 - x1, y2 - y1)
        sp = int(sp)
        sp = sp + 20

        if 30<sp<130 and y2>200:

            cv2.circle(img, (x1, y1), 6, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 100, 10), 3)
            spn1 = sp
            spn2 = sp
            while spn1 < spo:
                spo = spo - 1
                spo = str(spo)
                print(spo)
                arduino.write(bytes(spo, 'utf-8'))
                time.sleep(0.01)
                spo = int(spo)


            while spn2 > spo:
                spo = spo + 1
                spo = str(spo)
                print(spo)
                arduino.write(bytes(spo, 'utf-8'))
                time.sleep(0.01)
                spo = int(spo)


            spo = sp



        
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break