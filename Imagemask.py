import cv2
import numpy as np 


source_img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\download.jpg")
import_img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\Manas.png")

rows,column,channel=source_img.shape
roi=import_img[0:rows,0:column]

grayscale_source_img=cv2.cvtColor(source_img,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(grayscale_source_img,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)
bground_image=cv2.bitwise_and(roi ,roi ,mask=mask_inv)
fground_image=cv2.bitwise_and(source_img,source_img,mask=mask)


final_image=cv2.add(bground_image,fground_image)
import_img[0:rows,0:column]=final_image

cv2.imshow("Image",mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
