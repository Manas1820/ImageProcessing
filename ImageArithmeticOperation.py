import cv2
import numpy as np


img1=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\opencv-addWeighted-tutorial.png",cv2.IMREAD_UNCHANGED)
img2=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\download_1.jpg",cv2.IMREAD_UNCHANGED)
img3=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\mainlogo.png",cv2.IMREAD_UNCHANGED)

# add=img1+img2 this a method to add fully two solid images together without any transparency
# add=cv2.add(img1,img2) this method basically does addition of pixel of two image and the resultant is quite useless
#add=cv2.addWeighted(img1,0.4,img2,0.6,0) 

#cv2.imshow("Image",img3)
#cv2.imshow('res',img1)
#cv2.waitKey(0)
rows,column,channel =img3.shape
roi=img1[0:rows,0:column]

img2gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

bground=cv2.bitwise_and(roi, roi,mask=mask_inv)

fground=cv2.bitwise_and(img3, img3,mask=mask)

finalImage=cv2.add(bground,fground)
img1[0:rows ,0:column]= finalImage

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
