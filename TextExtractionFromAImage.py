import pytesseract as ps
import cv2

ps.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img=cv2.imread(r"C:\Users\gupta\OneDrive\Desktop\Image Processing\Images\15_15.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(ps.image_to_string(img))

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




