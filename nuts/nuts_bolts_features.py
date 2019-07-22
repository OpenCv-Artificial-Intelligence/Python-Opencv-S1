import cv2
import numpy as np
import math

def computeSolidity(contours):
	solid_list = []
	for c in contours:
		area = cv2.contourArea(c)
		hull = cv2.convexHull(c)
		hull_area = cv2.contourArea(hull)
		solidity = float(area)/hull_area
		solid_list.append(solidity)
	return solid_list
	
def computeAspectRatio(contours):
	ratio_list = []
	for c in contours:
		(center, size, angle) = cv2.minAreaRect(c)
		ratio = min(size)/max(size)
		ratio_list.append(ratio)
	return ratio_list

def createFeature(contours, category):
	ratio_list = computeAspectRatio(contours)
	solid_list = computeSolidity(contours)
	feature_list = []
	for x in range(len(ratio_list)):
		feature_list.append([ratio_list[x],solid_list[x],category])
	return feature_list
	
nuts = cv2.imread("Test images\\nuts.jpg")
bolts = cv2.imread("Test images\\bolts.jpg")
cv2.imshow("nuts", nuts)
cv2.imshow("bolts", bolts)
gray_nuts = cv2.cvtColor(nuts, cv2.COLOR_BGR2GRAY)
gray_bolts = cv2.cvtColor(bolts, cv2.COLOR_BGR2GRAY)
cv2.imshow("nuts - gray", gray_nuts)
cv2.imshow("bolts - gray", gray_nuts)
ret,binary_nuts = cv2.threshold(gray_nuts,240,255, cv2.THRESH_BINARY_INV)
ret,binary_bolts = cv2.threshold(gray_bolts,240,255, cv2.THRESH_BINARY_INV)
cv2.imshow("nuts - binary", binary_nuts)
cv2.imshow("bolts - binary", binary_bolts)

kernel3 = np.ones((3,3),np.uint8)
kernel5 = np.ones((5,5),np.uint8)

closed_nuts = cv2.morphologyEx(binary_nuts, cv2.MORPH_CLOSE, kernel5)
closed_bolts = cv2.morphologyEx(binary_bolts, cv2.MORPH_CLOSE, kernel5)
cv2.imshow("nuts - closed", closed_nuts)
cv2.imshow("bolts - closed", closed_bolts)

nuts_draw = nuts.copy()
bolts_draw = bolts.copy()
im1, nuts_contours, nuts_hierarchy = cv2.findContours(closed_nuts,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
im2, bolts_contours, bolts_hierarchy = cv2.findContours(closed_bolts,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(nuts_draw, nuts_contours, -1, (0,255,0))
cv2.drawContours(bolts_draw, bolts_contours, -1, (0,255,0))
cv2.imshow("nuts - contours", nuts_draw)
cv2.imshow("bolts - contours", bolts_draw)

nuts_feature = createFeature(nuts_contours, "nut")
bolts_feature = createFeature(bolts_contours, "bolt")


cv2.waitKey(0)
cv2.destroyAllWindows()
