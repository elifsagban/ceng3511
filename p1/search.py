import re
import sys
from collections import defaultdict


########### READING AND PARSING THE FILE ############

txt_values = []
txt_keys = []
filehandle = open(sys.argv[1], 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    txt_values.append(re.findall(r'\d+', line))
    txt_keys.append(line.split(':')[0])


filehandle.close()


###### FORMATTING ARRAY TO A DICTIONARY  ######

keys_and_values = {} # nested dict for keep the edges and their cost.

for line in range(txt_values.__len__()):
    inner_nodes = {}
    outer_nodes = {}

    for node in range(txt_values[line].__len__()):
        if txt_values[line][node] is not '0':

            inner_nodes[txt_keys[node]] = txt_values[line][node]

    outer_nodes = inner_nodes
    keys_and_values[txt_keys[line]] = outer_nodes


#for item in keys_and_values:
 #   print("Key : {} and values : {}".format(item, keys_and_values[item]))


######  GRAPH IS FOR UNIFORM COST SEARCH  #####


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight




# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return start

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


def ucs(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


####### DEPTH FIRST SEARCH #######
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


ucs_tuple = ()  # our dict format is not usable for ucs algorithm. The algorithm uses graph and this for the convertion
for item in keys_and_values:
    for j in keys_and_values[item]:
        ucs_tuple = ucs_tuple + ((item, j, int(keys_and_values[item][j])),)  # ('A', 'B', 6)


graph_ucs = Graph()  # tuple to graph


for edge in ucs_tuple:
    graph_ucs.add_edge(*edge)

##### User Input and Exception Handling #####
while True:
        start = input("Please enter the start state : ")
        goal = input("Please enter the goal state : ")
        is_valid = False

        if (len(start)<1 and len(start)>1):
            print("Not valid! Please enter one start state.")
            continue
        elif (len(goal)<1 and len(goal)>1):
            print("Not valid! Please enter one goal state.")
            continue
        elif re.search("[a-z]", start):
            print("Not valid! Please enter an uppercase letter.")
            continue
        elif re.search("[a-z]", goal):
            print("Not valid! Please enter an uppercase letter.")
            continue
        elif re.search("[~!'^#+$%&½/{*?}[\-.,;:<£>]",start):
            print("Not valid! Please enter only letter.")
            continue
        elif re.search("[~!'^#+$%&½/{*?}[\-.,;:<£>]",goal):
            print("Not valid! Please enter only letter.")
            continue
        elif re.search("[\s]",start):
            print("Not valid! Please do not enter a space.")
            continue
        elif re.search("[\s]",goal):
            print("Not valid! Please do not enter a space.")
            continue
        else:
            is_valid = True
            break


print("BFS : " + " - ".join(bfs_shortest_path(keys_and_values, start, goal)))
print("DFS : " + " - ".join(dfs_paths(keys_and_values, start, goal)))
print("UCS : " + " - ".join(ucs(graph_ucs, start, goal)))


