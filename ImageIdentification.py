import cv2
import matplotlib.pyplot as plt 
import numpy as np 

img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Manas.PNG",cv2.IMREAD_COLOR)
# To draw a line
cv2.line(img ,(0,0),(100,100) ,(0,0,0),20)
#to draw an rectangle
cv2.rectangle(img,(0,0),(250,250),(0,255,0),5)
#To draw a circle
cv2.circle(img,(187,187),100,(255,0,0),-1) #-1 is used to fill the circle
# To draw a polygon on an image
pts=np.array([[0,0],[50,100],[100,50]], np.int32)
#pts=pts.reshape(1,-2,1)
cv2.polylines(img,[pts],True,(255,0,255),5)
#To write on an image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img," FUCK ME ! ",(0,130),font,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()