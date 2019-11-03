import cv2
import numpy as np

#creating using 3 channels
img=np.zeros((512,512,3),np.uint8)
img_bw=np.zeros((512,512),np.uint8)

cv2.line(img,(0,0),(511,511),(255,127,0),5)
#location,start,end,colour,thickness

cv2.imshow("colour",img)
cv2.imshow("b&w",img_bw)

cv2.waitKey()
cv2.destroyAllWindows()