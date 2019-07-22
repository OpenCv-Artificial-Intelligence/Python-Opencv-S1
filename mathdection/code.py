#use python 2.7 , opencv

import cv2
import math

#Load image
img = cv2.imread('Make_with_paint.png')
#cv2.imshow('img',img)

#Convert RGB to Gray Scale
img_gray = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
#cv2.imshow('img_gray',img_gray)

#threshold 0-60 set to 0(Black Color) :: 60-255 set to 255(White color) 
img_thresh = cv2.threshold(img_gray.copy(),60,255,cv2.THRESH_BINARY)[1]
#cv2.imshow('img_thresh',img_thresh)

#findContours return image, contours, hierarchy
#cnts = [image, contours, hierarchy]
cnts = cv2.findContours(img_thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#select contours
cnts2 = cnts[1]

#Loop contours
for i in range(0,len(cnts2)):
    #The distance along the curved line
    peri = cv2.arcLength(cnts2[i],True)

    #list corner
    approx = cv2.approxPolyDP(cnts2[i],0.04 * peri,True)

    #find center of contours
    M = cv2.moments(cnts2[i])
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    
    #output text to image
    cv2.putText(img,'No. ' + str(i),(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.putText(img,str(len(approx)),(approx[0][0][0],approx[0][0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    #Draw 
    #cv2.drawContours(img,cnts2[i],-1,(0,0,255),2)
    
    #for x in range(0,len(approx)):
    #    cv2.putText(img,'.',(approx[x][0][0],approx[x][0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)


cv2.imshow('img contours',img)

#q to exit()
while 1:
    c = cv2.waitKey(0)
    if chr(c & 255) == 'q':
        break
cv2.destroyAllWindows()






