class Vertex():
    def __init__(self, name):
        self.name = name
        self.neighbors = []


class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices

    def add_vertex(self, v):
        self.vertices.append(v)

    def add_edge(self, v, e):
        for i in range(len(self.vertices)):
            if self.vertices[i] == v:
                v.neighbors.append(e)

    def printGraph(self):
        dictionary = {}
        list = []
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices[i].neighbors)):
                list.append(self.vertices[i].neighbors[j].name)
            dictionary[self.vertices[i].name] = list
        print(dictionary)


""""
class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        self.vertices[v.name] = v

    def add_edge(self, v, e):
        self.vertices[v].neighbors.append(self.vertices(e))
"""


def BFS(graph, start):
    q = []
    tabu = set()
    q.append(start)
    tabu.add(start)

    while not q == []:
        v = q.pop(0)
        print(v)
        for node in graph[v]:
            if not node in tabu:
                tabu.add(node)
                q.append(node)


def unweighted_shortest_pathCost(graph, start):
    cost = {}
    q = []
    tabu = set()
    q.append(start)
    tabu.add(start)
    cost[start] = 0

    while not q == []:
        v = q.pop(0)
        for node in graph[v]:
            if not node in tabu:
                tabu.add(node)
                q.append(node)
                cost[node] = cost[v] + 1

    return cost


def unweighted_shortest_path(graph, start):
    path = {}
    q = []
    tabu = set()
    q.append(start)
    tabu.add(start)
    for i in graph:
        path[i] = [start]
    while not q == []:
        v = q.pop(0)
        for node in graph[v]:
            if not node in tabu:
                tabu.add(node)
                q.append(node)
                if not v in path[node]:
                    path[node].append(v)
    for i in graph:
        path[i].append(i)
    return path






g = \
{'A': ['B','C'],
   'B': ['A','D','C'],
   'C': ['A','B','D','E'],
   'D': ['B','C','E','F'],
   'E': ['C','D','F'],
   'F': ['D','E']}



dict = unweighted_shortest_pathCost(g, 'D')
print(dict)

dict2 = unweighted_shortest_path(g, 'A')
print(dict2)
"""
test = Graph()
test.add_vertex(Vertex('A'))
test.add_vertex(Vertex('B'))
test.add_vertex(Vertex('C'))
test.add_vertex(Vertex('D'))
test.add_vertex(Vertex('E'))
test.add_vertex(Vertex('F'))
test.add_vertex(Vertex('G'))
test.add_edge(test.vertices[0], test.vertices[1])
test.add_edge(test.vertices[0], test.vertices[2])
test.add_edge(test.vertices[1], test.vertices[0])
test.add_edge(test.vertices[1], test.vertices[3])
test.add_edge(test.vertices[1], test.vertices[4])
test.add_edge(test.vertices[2], test.vertices[0])
test.add_edge(test.vertices[2], test.vertices[1])
test.add_edge(test.vertices[2], test.vertices[3])
test.add_edge(test.vertices[2], test.vertices[4])
test.add_edge(test.vertices[3], test.vertices[1])
test.add_edge(test.vertices[3], test.vertices[2])
test.add_edge(test.vertices[3], test.vertices[4])
test.add_edge(test.vertices[3], test.vertices[5])
test.add_edge(test.vertices[4], test.vertices[2])
test.add_edge(test.vertices[4], test.vertices[3])
test.add_edge(test.vertices[4], test.vertices[5])
test.add_edge(test.vertices[5], test.vertices[3])
test.add_edge(test.vertices[5], test.vertices[4])
"""
