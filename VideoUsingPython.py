import cv2
import matplotlib.pyplot as plt
import numpy as np


cap=cv2.VideoCapture(0)
#fourcc =cv2.VideoWriter_fourcc(*'XVID')    # To save a file
#out=cv2.VideoWriter('FirstVideoUsingPython',fourcc,20.0,(640,480))
while True :
    ret,frame =cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #cvt is used for convert
    cv2.imshow("Frame",frame)
    #out.write(frame)
    cv2.imshow("Gray",gray)
    if cv2.waitKey(1) & 0xFF == ord('q') : #   this basically means that when you press q it will exit the screen
        break
cap.release()
#out.release()
cv2.destroyAllWindows()


