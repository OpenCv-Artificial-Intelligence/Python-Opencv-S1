import sys
import cv2
import cv2 as cv
import numpy as np


frame = cv2.imread("perspective.png")

#left top 
frame = cv2.rectangle(frame,(230,255),(340,365),(0,255,0),2)

#right top
frame = cv2.rectangle(frame,(605,255),(720,370),(0,255,0),2)

#center
#img = cv2.rectangle(img,(xleft,ytop),(w,h),(0,255,0),5)
frame = cv2.rectangle(frame,(415,445),(525,560),(0,255,0),2)

#left top
frame = cv2.rectangle(frame,(230,630),(340,735),(0,255,0),2)

#right buttom
frame = cv2.rectangle(frame,(595,630),(710,740),(0,255,0),2)


#cv2.circle(frame, (x-position-left, y-positon-formtop-to-butom-heigh), 5, (0, 0, 255), -1)
cv2.circle(frame, (210, 240), 5, (0, 0, 255), -1)
cv2.circle(frame, (730, 240), 5, (0, 0, 255), -1)
cv2.circle(frame, (210, 745), 5, (0, 0, 255), -1)
cv2.circle(frame, (730, 745), 5, (0, 0, 255), -1)

#pts1 = np.float32([[valuefram1, valuefram1], [valuefram2, valuefram2], [valuefram3, valuefram3], [valuefram4, valuefram4]])
pts1 = np.float32([[225, 250], [720, 255], [230, 735], [710, 740]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(frame, matrix, (500, 600))


cv2.imshow("Frame", frame)
cv2.imshow("Perspective transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
