import cv2
import numpy as np

template = cv2.imread(r'C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\Manas.PNG')
cap=cv2.VideoCapture(0)
w, h = template.shape[::-1]
while(1) :
    _,frame=cap.read()

    frame_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    res = cv2.matchTemplate(frame_gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = 0.8

    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255,0,255), 2)
    cv2.imshow('Detected',frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break    

cap.release()
cv2.destroyAllWindows()

