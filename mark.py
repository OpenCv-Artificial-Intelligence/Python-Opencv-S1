import cv2
import numpy as np

img = cv2.imread("perspective.png")

#crop_img = img[y:y+h, x:x+w]
#img = cv2.rectangle(img,(220,220),(400,400),(0,255,0),2)

#left top 
img = cv2.rectangle(img,(230,255),(340,365),(0,255,0),5)

#right top
img = cv2.rectangle(img,(605,255),(720,370),(0,255,0),5)

#center
#img = cv2.rectangle(img,(xleft,ytop),(w,h),(0,255,0),5)
img = cv2.rectangle(img,(415,445),(525,560),(0,255,0),5)

#left top
img = cv2.rectangle(img,(230,630),(340,735),(0,255,0),5)

#right buttom
img = cv2.rectangle(img,(605,630),(720,735),(0,255,0),5)


    cv2.circle(frame, (155, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (480, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (20, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (620, 475), 5, (0, 0, 255), -1)

pts1 = np.float32([[230, 120], [480, 120], [20, 475], [620, 475]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(frame, matrix, (500, 600))


cv2.imshow("cropped", img)
cv2.imshow("Perspective transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

