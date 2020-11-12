import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

def printIMG(image):
    cv2.imshow("Image",image)
    cv2.waitKey()

shape = "unidentified"

rez = cv2.imread("img/rez.jpg")

blue_upper = np.array([255, 65, 65])
blue_lower = np.array([200, 0, 0])

red_upper = np.array([65, 65, 255])
red_lower = np.array([0, 0, 200])

green_upper = np.array([65, 255, 65])
green_lower = np.array([0, 200, 0])

white_upper = np.array([255, 255, 255])
white_lower = np.array([200, 200, 200])

black_upper = np.array([65, 65, 65])
black_lower = np.array([0, 0, 0])

upper = red_upper
lower = red_lower

mask = cv2.inRange(rez, lower, upper)
img, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c = max(cnts, key=cv2.contourArea)
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.04 * peri, True)
cv2.drawContours(rez, [approx], -1, (0, 255, 0), 4)

if len(approx) == 4:
    # compute the bounding box of the contour and use the
    # bounding box to compute the aspect ratio
    (x, y, w, h) = cv2.boundingRect(approx)
    ar = w / float(h)
    # a square will have an aspect ratio that is approximately
    # equal to one, otherwise, the shape is a rectangle
    shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    # if the shape is a pentagon, it will have 5 vertices
    print(shape)

printIMG(rez)
cv2.imwrite("img/redFound.jpg",rez)

cv2.destroyAllWindows()