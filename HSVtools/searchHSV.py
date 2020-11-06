import numpy as np
import imutils
import cv2

green = np.uint8([[[0,128,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

#rgb 0,255,0 
#low 50,122,129 + 10,100,100 to high

#high 60,255,255 - 10,100,100 to low
#[[[ 60 255 255]]]
