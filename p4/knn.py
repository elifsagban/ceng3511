import csv
import math
import operator
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



data = pd.read_csv('./train.csv', delimiter = ',', names=['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep',
'mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range'])[1:]
data2 = pd.read_csv('./test.csv', delimiter = ',', names=['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep',
'mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range'])[1:]

df = pd.DataFrame(data)
x = df.to_numpy()
trainingSet = x.astype(float)

df2 = pd.DataFrame(data2)
x2 = df2.to_numpy()
testSet = x2.astype(float)
#print(testSet)

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(2,length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):

        neighbors.append(distances[x][0][20])

    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1),  reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0

    for w in range(len(testSet)):
        if testSet[w][-1] == predictions[w]:
            correct += 1

    return correct, (correct/float(len(testSet) )) * 100


# prepare data

print ('Train set: ' + repr(len(trainingSet)))
print ('Test set: ' + repr(len(testSet)))
# generate predictions
y_coordinate = []
k = 10
k_neighbors_price_ranges = []

for x in range(len(testSet)):
    k_neighbors_price_range = getNeighbors(trainingSet, testSet[x], k)
    k_neighbors_price_ranges.append(k_neighbors_price_range)

for j in range(1, k + 1):
    predictions = []
    print("k: ", j)
    for i in range(len(k_neighbors_price_ranges)):
        result = getResponse(k_neighbors_price_ranges[i][0:j])
        predictions.append(result)
            # print('Predicted: ' + str(result) + "  >>  ", "Actual: " + str(test_set[i][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + str(accuracy) + "%\n")
    y_coordinate.append(accuracy)

f = plt.figure(figsize=(10,6))
plt.plot(range(1, 11),y_coordinate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
# plt.show()
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
f.savefig("plot.pdf")


#for x in range(len(testSet)):
#    neighbors = getNeighbors(trainingSet, testSet[x], k)
 #   result = getResponse(neighbors)
#    predictions.append(result)

