#cv version 3.4.2
import sys
import cv2
import cv2 as cv
import numpy as np

images = "pic/3"

original = cv2.imread(images+".jpg")
img = cv2.imread(images+".jpg",0)
src = cv2.imread(images+".jpg", cv.IMREAD_COLOR)

# Create mask
height,width = img.shape
mask = np.zeros((height,width), np.uint8)

# Create mask thresh for equl 1 
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Create mask thresh for equl 2
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,200)

if circles is not None:
    for i in circles[0,:]:
        circles = np.uint16(np.around(circles))
        center = (i[0], i[1])
        i[2]=i[2]+4
        
        # Draw on mask
        cv2.circle(mask,(i[0],i[1]),i[2],(255,255,255),thickness=-1)
        
        # circle center
        #cv.circle(original, center, 1, (0, 255, 0), 5)
        
        # circle outline
        radius = i[2]
        #cv.circle(original, center, radius, (0, 255, 0), 1)

# Copy that image using that mask
masked_data = cv2.bitwise_and(original, original, mask=mask)
#print(masked_data)

# Apply Threshold
_,threshs = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)

# Find Contour
contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])

# Crop masked_data
crop = masked_data[y:y+h,x:x+w]
#print(crop)

# Crop and wirte image
#cv2.imshow('Original Picture',original)
#cv2.imshow('gray Picture',gray)
#cv2.imshow('threshs Picture',threshs)
#cv2.imshow('Cropped Picture',crop)

# resize image
print('Original Dimensions : ',crop.shape)
scale_percent = 145 # percent of original size
width = int(crop.shape[1] * scale_percent / 100)
height = int(crop.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)
# resize image
#cv2.imshow("Resized image", resized)

rows, cols, ch = resized.shape
#print('Resized rows and cols : ',rows,cols)

#cv2.circle(, (x-position-left, y-positon-formtop-to-butom-heigh), 5, (0, 0, 255), -1)

#left top 
frame = cv2.rectangle(resized,(230,255),(340,365),(0,255,0),2)

#right top
frame = cv2.rectangle(resized,(605,255),(720,370),(0,255,0),2)

#center
#img = cv2.rectangle(img,(xleft,ytop),(w,h),(0,255,0),5)
frame = cv2.rectangle(resized,(415,445),(525,560),(0,255,0),2)

#left top
frame = cv2.rectangle(resized,(230,630),(340,735),(0,255,0),2)

#right buttom
frame = cv2.rectangle(resized,(595,630),(710,740),(0,255,0),2)


#left top
cv2.circle(resized, (220, 210), 5, (0, 0, 255), -1)
#right top
cv2.circle(resized, (730, 210), 5, (0, 0, 255), -1)
#center
#cv2.circle(resized, (470, 450), 5, (0, 0, 255), -1)
#left buttom
cv2.circle(resized, (210, 745), 5, (0, 0, 255), -1)
#right buttom
cv2.circle(resized, (730, 745), 5, (0, 0, 255), -1)

#pts1 = np.float32([[valuefram1, valuefram1], [valuefram2, valuefram2], [valuefram3, valuefram3], [valuefram4, valuefram4]])
pts1 = np.float32([ [210, 240], [730, 240], [210, 745]])
pts2 = np.float32([ [210, 240], [730, 240], [210, 745]])

matrix = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(resized, matrix, (cols, rows))

cv2.imshow("Perspective", result)

pts11 = np.float32([[220, 210], [730, 210], [210, 745], [730, 745]])
pts22 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
matrix = cv2.getPerspectiveTransform(pts11, pts22)

resultwrap = cv2.warpPerspective(resized, matrix, (cols, rows))


cv2.imshow("Perspective transformation", resultwrap)
#Code to close Window
cv2.waitKey(0)
cv2.destroyAllWindows()
