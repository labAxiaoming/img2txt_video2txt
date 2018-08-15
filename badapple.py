# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:46:28 2018

@author: Administrator
"""
import cv2
import os
import numpy as np
import time

#########################
def clear():
    os.system('cls')
#    i=np.random.randint(1,9)   #换颜色
#    os.system('color 0%d'%(i)) #换颜色


def img2txt(img):
    serarr=['@','#','$','%','&','?','*','o','/','{','[','(','|','!','^','~','-','_',':',';',',','.','`',' ']
    count=len(serarr)
     
#    def toText(image_file):
#    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转灰度
    low=np.array([200,200,200])
    up=np.array([255,255,255])
    
    img=cv2.inRange(img,low,up)
    img=cv2.resize(img,(70,55))
    asd =''#储存字符串
    for h in range(img.shape[0]):#h
       for w in range(img.shape[1]):#w
          gray =img[h,w]
          asd=asd+serarr[int(gray/(255/(count-1)))]
       asd=asd+'\r\n'
    print(asd)
     
#####################################
#cap = cv2.VideoCapture('E:/pythondemo/CV2/badapple/bd.mp4')
cap = cv2.VideoCapture('bd.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)  
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5)
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)
fourcc=cv2.VideoWriter_fourcc(*'I420')
size = (width,height)  
ret, frame = cap.read()

i=0 
while(cap.isOpened()):
    i+=1
    if i%60==0:
#        cv2.imwrite('img/10000000+%d.jpg'%(i),frame)    
        ret, frame = cap.read()
        clear()
#        os.system('cls')
        img2txt(frame)
        time.sleep(0.1)
#    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

#python badapple.py


#python badapple.py





