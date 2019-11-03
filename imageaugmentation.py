import numpy as np
import matplotlib.pyplot as plt
import cv2

name=1
for i in range(1,16,1):
   img=cv2.imread('pos-'+str(i)+'.jpg')
   (w,h)=img.shape[:2]
   for angle in range(45,360,45):
        M=cv2.getRotationMatrix2D((w/2,h/2),angle,1.0)
        image=cv2.warpAffine(img,M,(w,h))
        cv2.imwrite(str(name)+'.jpg',image)
        name+=1
        
    M = np.float32([[1,0,w/3],[0,1,0]])
    image = cv2.warpAffine(img,M,(h,w))
   cv2.imwrite(str(name)+'.jpg',image)
   name+=1
    M = np.float32([[1,0,-w/3],[0,1,0]])
    image = cv2.warpAffine(img,M,(h,w))
    cv2.imwrite(str(name)+'.jpg',image)
    name+=1
    
    image = cv2.resize(img,None,fx=0.5,fy=0.5)
    cv2.imwrite(str(name)+'.jpg',image)
    name+=1
 

    image = cv2.resize(img,None,fx=2,fy=2)
    cv2.imwrite(str(name)+'.jpg',image)
    name+=1
    image = cv2.flip( img, 0 )
    cv2.imwrite(str(name)+'.jpg',image)
    name+=1 
    image= cv2.flip( img, 1 )
    cv2.imwrite(str(name)+'.jpg',image)
    name+=1 
    
