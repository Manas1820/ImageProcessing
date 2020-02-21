import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("images.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR =1
#IMREAD_UNCHANGED =-1

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''plt.imshow(img ,cmap='gray' ,interpolation='bicubic') 
plt.plot([500,100],[80,100],'c',linewidth=5)
plt.show()'''