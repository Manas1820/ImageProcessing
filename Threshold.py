import cv2
import numpy as np 


img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\bookpage.jpg")
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold =cv2.threshold(img,10,255,cv2.THRESH_BINARY)
retval1,grayscale_threshold =cv2.threshold(grayscale,10,255,cv2.THRESH_BINARY)
grayscale_adaptive_threshold= cv2.adaptiveThreshold(grayscale, 220, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#cv2.imshow("IMAGE",img)
#cv2.imshow("Gray Image",grayscale_threshold)
cv2.imshow("THRES IMAGE",grayscale_adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()


