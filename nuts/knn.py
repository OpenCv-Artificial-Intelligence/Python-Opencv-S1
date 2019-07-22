import csv
import cv2
import numpy as np
import math
import operator

# compute euclidean distance of 2 instances (points in space)
def euclideanDistance(data1, data2, length):
	distance = 0
	for x in range(length):
		distance += pow((data1[x] - data2[x]),2)
	return math.sqrt(distance)

# return a list of k nearest neighbors between the test instance and the points in training set
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

# find the maximum votes in the list
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]	
