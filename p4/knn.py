import csv
import random
import math
import operator
import numpy as np
import pandas as pd

data = pd.read_csv('./train.txt', delimiter = ',', names=['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep',
'mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range'])[1:]
data2 = pd.read_csv('./test.txt', delimiter = ',', names=['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep',
'mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range'])[1:]

df = pd.DataFrame(data)
x = df.to_numpy()
trainingSet = x.astype(np.float)

df2 = pd.DataFrame(data2)
x2 = df2.to_numpy()
testSet = x2.astype(np.float)

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(2,length):
		#print(instance1[x],instance2[x])
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
		#print(distance)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	print(testInstance)
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
		#print("neighbors")
		#print(neighbors)
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	#print(classVotes)
	sortedVotes = sorted(classVotes, key=operator.itemgetter(1), reverse=True)
	#print(sortedVotes)
	return sortedVotes[0][0:]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	

# prepare data

print ('Train set: ' + repr(len(trainingSet)))
print ('Test set: ' + repr(len(testSet)))
# generate predictions
predictions=[]
k = 10


for x in range(len(testSet)):
	neighbors = getNeighbors(trainingSet, testSet[x], k)
	result = getResponse(neighbors)
	predictions.append(result)
	print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][1]))

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
