import cv2
import numpy as np


# this is to remove diffrent type of noise

cap=cv2.VideoCapture(0)

while(1) :
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    


    lower_red=np.array([150,150,50])
    upper_red=np.array([255,255,180])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    # to add a bit of blur 
    kernel=np.ones((15,15),np.float32)/255
    smoothed=cv2.filter2D(res,-1,kernel) 

    blur=cv2.GaussianBlur(res,(15,15),0)

    median=cv2.medianBlur(res,15) 

    bilateral=cv2.bilateralFilter(res,15,75,75)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('smoothed',smoothed)
    #cv2.imshow('GaussianBlur',blur)
    cv2.imshow('MedianBlur',median)
    #cv2.imshow('bilateral',bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()   