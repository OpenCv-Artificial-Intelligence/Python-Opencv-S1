import cv2
import numpy as np

img = cv2.imread('c.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_gray = np.array([0, 5, 50], np.uint8)
upper_gray = np.array([350, 50, 255], np.uint8)

mask = cv2.inRange(hsv, lower_gray, upper_gray)
img_res = cv2.bitwise_and(img, img, mask = mask)
cv2.imwrite('gray.png',img_res)
