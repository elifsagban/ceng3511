import pandas as pd
import numpy as np
import plotly.offline as plt
import plotly.graph_objs as go
from math import sqrt
from random import randrange
import math as m
import operator




##for line in file.readlines()[1:]:
 ##   fname = line.rstrip().split(',') #using rstrip to remove the \n
  ##  print(fname)

##names=['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep',
##'mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range']


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
		#print(instance1[x],instance2[x],type(instance1[x]))
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return m.sqrt(distance)

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
	return neighbors
	


"""
#min-max
def dataset_minmax(y):
	minmax = list()
	for i in range(len(y[0])):
		col_values = [row[i] for row in y]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax
# Rescale dataset columns to the range 0-1
def normalize_dataset(y, minmax):
	for row in y:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Split a dataset into k folds
def cross_validation_split(y, n_folds):
	dataset_split = list()
	dataset_copy = list(y)
	fold_size = int(len(y) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(y, algorithm, n_folds, *args):
	folds = cross_validation_split(y, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbors)
		predictions.append(output)
	return(predictions)

def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

prediction = predict_classification(y, y[0], 10)
print('Expected %d, Got %d.' % (y[0][-1], prediction))

"""