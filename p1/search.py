import re
import sys
#filename = "graph.txt"
graph = 'C:\\Users\\bk\\Desktop\\ceng3511\\p1\\graph.txt'

# open the file for reading
filehandle = open(sys.argv[1], 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    result = re.findall(r'\d+', line)
    print(result)

# test2
filehandle.close()
#
#
# # visits all the nodes of a graph (connected component) using BFS
# def bfs_connected_component(graph, start):
#     # keep track of all visited nodes
#     explored = []
#     # keep track of nodes to be checked
#     queue = [start]
#
#     # keep looping until there are nodes still to be checked
#     while queue:
#         # pop shallowest node (first node) from queue
#         node = queue.pop(0)
#         if node not in explored:
#             # add node to list of checked nodes
#             explored.append(node)
#             neighbours = graph[node]
#
#             # add neighbours of node to queue
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#     return explored
#
#
# bfs_connected_component(graph, 'A')  # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']





#string1 - Result: 3.11899876595
#string2 - Result: 2.78014397621
#The above results are a product of the lowest