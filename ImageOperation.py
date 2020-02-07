import numpy as np
import cv2

img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Manas.PNG",cv2.IMREAD_COLOR)

px=img[55,55]

img[55,55]=[255,255,255]
print(px)

#roi =img[27:301 ,100:310] =[0,255,255]
my_face =img[27:301 ,100:310]
img[0:274,0:210] =my_face

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()