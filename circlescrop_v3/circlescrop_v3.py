import cv2
import numpy as np

images = "pic/2.jpg";

img1 = cv2.imread(images)
img = cv2.imread(images,0)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Create mask
height,width = img.shape
mask = np.zeros((height,width), np.uint8)

edges = cv2.Canny(thresh, 100, 200)
#cv2.imshow('detected ',gray)
cimg=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 10000, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)
for i in circles[0,:]:
    i[2]=i[2]+4
    # Draw on mask
    cv2.circle(mask,(i[0],i[1]),i[2],(255,255,255),thickness=-1)

# Copy that image using that mask
masked_data = cv2.bitwise_and(img1, img1, mask=mask)

# Apply Threshold
_,thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)

# Find Contour
contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])

# Crop masked_data
crop = masked_data[y:y+h,x:x+w]

#Code to close Window
cv2.imshow('detected',img1)
cv2.imshow('Cropped',crop)
cv2.imwrite('filecrop.jpg', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
