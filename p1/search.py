import re
import sys


result = []
keys = []
filehandle = open(sys.argv[1], 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    result.append(re.findall(r'\d+', line))
    keys.append(line.split(':')[0])


filehandle.close()

keys_and_values = {}

for line in range(result.__len__()):
    sum_nodes = {}
    node_list = {}

    for node in range(result[line].__len__()):
        if result[line][node] is not '0':

            sum_nodes[keys[node]] = result[line][node]

    node_list = sum_nodes

    keys_and_values[keys[line]] = node_list


for item in keys_and_values:
    print("Key : {} and values : {}".format(item, keys_and_values[item]))


print(keys_and_values['A'].keys())


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


start = input("Please enter the start state :")
goal = input("Please enter the goal state :")

print(bfs_shortest_path(keys_and_values, start, goal))



