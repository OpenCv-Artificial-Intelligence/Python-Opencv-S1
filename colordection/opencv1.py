#python 2.7 , opencv 3.3
import cv2
import numpy as np

image = cv2.imread('color_pencil.jpg')
cv2.imshow('show image',image)

img_output = image.copy()
image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_range = np.array([115,50,100], dtype=np.uint8)
upper_range = np.array([130,255,255], dtype=np.uint8)

img_segment = cv2.inRange(image.copy(),lower_range,upper_range)
img_segment = cv2.morphologyEx(img_segment,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))
_,contours, hi = cv2.findContours(img_segment,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for index in range(0,len(contours)):
    x,y,w,h = cv2.boundingRect(contours[index])
    cv2.rectangle(img_output,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('show segment',img_segment)
cv2.imshow('show output',img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
