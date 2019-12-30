import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# reading data
data = open('data.txt', 'r')
next(data)
X = []
f = data.readlines()
for line in f:
    arr = line.rstrip().split(",")
    X.append([int(arr[0]), int(arr[1])])




def euclidian(x_dist, y_dist):
    distance = 0
    for w in range(len(x_dist)):
        distance += (x_dist[w] - y_dist[w]) ** 2
    distance = np.sqrt(distance)
    return distance

def random_centers(X , K):
    centers = []
    point = np.random.randint(0, len(X))
    centers.append(X[point])
    dist = np.zeros(len(X))  # return a desired array filled with zeros
    for c in range(K-1):
        for i in range(len(X)):
            dist[i] += euclidian(centers[len(centers)-1], X[i])
        point = np.argmax(dist)   # gets max distance for random selection
        centers.append(X[point])
    return centers


def mean_function(X, centers):
    n = len(centers)
    s = [0] * len(X[0])
    for i in range(n):
        for j in range(len(X[0])):
            s[j] += X[centers[i]][j]
    for j in range(len(X[0])):
        s[j] /= n
    return s


def main_kmeans(X, k, iter_num=100):
    updated_centers = random_centers(X, k)
    for lp in range(iter_num):
        cluster = []
        for i in range(k):
            cluster.append([])
        for i in range(len(X)):
            min_idx = 0
            min_dis = 999999
            for j in range(k):
                d = euclidian(updated_centers[j] ,X[i])
                if d < min_dis:
                    min_idx = j
                    min_dis = d
            cluster[min_idx].append(i)
        for i in range(k):
            if len(cluster[i]) != 0:
                updated_centers[i] = mean_function(X, cluster[i])
    return [cluster, updated_centers]


color = ['red', 'goldenrod', 'maroon', 'cyan', 'darkorange']
markers = [',', 'x', '+', 'v', 'o']


def call_function(result, centers,  ax, k):
    for i in range(len(result)):
        lst = []
        col = color[i]
        for j in range(len(result[i])):
            lst.append(X[result[i][j]])
        lst = pd.DataFrame(lst)
        ax.scatter(lst[0], lst[1], alpha=0.275, cmap='viridis')
        ax.scatter(centers[i][0], centers[i][1], marker=markers[i], color="black", alpha=1.0, s= 100)

        ax.set_title('result when k = ' + str(k))


# find multiple plots into one png, i took it from stackover flow.
fig = plt.figure(1)
sub1 = fig.add_subplot(323)
call_function(main_kmeans(X, 2, iter_num=10)[0],main_kmeans(X, 2, iter_num=10)[1], sub1, 2)

sub2 = fig.add_subplot(324)
call_function(main_kmeans(X, 3, iter_num=10)[0],main_kmeans(X, 3, iter_num=10)[1], sub2, 3)

sub3 = fig.add_subplot(325)
call_function(main_kmeans(X, 4, iter_num=10)[0],main_kmeans(X, 4, iter_num=10)[1], sub3, 4)

sub4 = fig.add_subplot(326)
call_function(main_kmeans(X, 5, iter_num=10)[0],main_kmeans(X, 5, iter_num=10)[1], sub4, 5)

plt.tight_layout()  # just to improve spacings
fig.savefig('plot.pdf')
