import heapq as hq
import math

g = \
{'A': [('B',3),('C',1)],
'B': [('A',3),('D',5),('C',7),('E',1)],
'C': [('A',1),('B',7),('D',2)], 
'D': [('B',5),('C',2),('E',7)],
'E': [('B',1),('D',7)]}

def dijkstra(graph, start):
    heap = []
    visited = set()
    cost = {}
    for i in graph:
        cost[i] = math.inf
    cost[start] = 0
    hq.heappush(heap, (0, start))
    while not heap == []:
        (costv, v) = hq.heappop(heap)
        if not v in visited:
            visited.add(v)
            for w in graph[v]:
                candcost = cost[v] + w[1]
                if candcost < cost[w[0]]:
                    cost[w[0]] = candcost
                    hq.heappush(heap, (candcost, w[0]))
    return cost


def dijkstraPrev(graph, start):
    heap = []
    visited = set()
    cost = {}
    prev = {}
    for i in graph:
        cost[i] = math.inf
    cost[start] = 0
    hq.heappush(heap, (0, start))
    while not heap == []:
        (costv, v) = hq.heappop(heap)
        if not v in visited:
            visited.add(v)
            for w in graph[v]:
                candcost = cost[v] + w[1]
                if candcost < cost[w[0]]:
                    cost[w[0]] = candcost
                    prev[w[0]] = v
                    hq.heappush(heap, (candcost, w[0]))
    return prev

def get_path(prev, end):
    x = end
    path = []
    while x in prev:
        path.append(x)
        x = prev[x]
    path.append(x)
    return path[::-1]
            

test = dijkstra(g, 'D')
test2 = dijkstraPrev(g, 'D')
path = get_path(test2, 'A')
print(test)
print(test2)
print(path)


