import cv2
import numpy as np


# this is to remove diffrent type of noise

cap=cv2.VideoCapture(1)

while(1) :
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    


    lower_red=np.array([150,150,50])
    upper_red=np.array([255,255,180])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    

    kernel=np.ones((1,1),np.uint8)
    #erosion=cv2.erode(mask ,kernel,iterations=1)#its a slider and removes unwanted color
    #dilation=cv2.dilate(mask ,kernel,iterations=1)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    #finalMask=erosion+dilation 
    finalImageMask=opening+closing
     
    res=cv2.bitwise_and(frame,frame,mask=finalImageMask)
    #res=cv2.bitwise_and(frame,frame,mask=finalMask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imshow('res',res)
   

   
 

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()   