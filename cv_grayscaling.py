import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Admin\Pictures\Camera Roll\butterfly.jpg') 
cv2.namedWindow("preview")
cv2.imshow("preview",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscaling",gray)
cv2.waitKey()
cv2.destroyAllWindows()