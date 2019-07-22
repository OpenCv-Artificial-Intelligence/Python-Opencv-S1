import numpy as np
import cv2

# Create a black image
#img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
#img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

#img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

img = cv2.imread('color.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

                          
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(0,0,255),2)

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
