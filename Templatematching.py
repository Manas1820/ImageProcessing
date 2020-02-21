import cv2
import numpy as np

img_rgb = cv2.imread(r'C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\SampleImage.jpg')

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#img_gray = np.array(img_gray, dtype=np.uint8)

template = cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\SampleImage1.jpg",0)
w, h = template.shape[::-1]

#print(w,h)

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,255), 2)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

