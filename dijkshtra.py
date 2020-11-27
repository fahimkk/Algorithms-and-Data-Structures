import math
import heapq
# positive wighted graph
adj_dict_1 = {'a':['b','c'],
              'b':['d','c'],
              'c':['b','d','e'],
              'd':['e'],
              'e':['d']}

adj_dict_2 = {'a':{'b':10,'c':3},
              'b':{'d':2,'c':1},
              'c':{'b':4,'d':8,'e':2},
              'd':{'e':7},
              'e':{'d':9}}
# for getting min weighted vertex, we use heap
# for priority que we can use heap with tuple, 
# to return in the order of they added for same element - 
# - add second element as count

# end is to find the path to the end vertex if end is given
def dijkshtra(adj_dict, s,end=False):
#    que_heap = [(math.inf, key) if key != s else (0,s) for key in adj_dic]
    que_heap = [(0,s)]
    # to relax (decreament) weight we need a data structure to compare,
    relaxation_dict = {key:math.inf if key !=s else 0 for key in adj_dict}
    visited = set()
    parent={s:None} # not neccessary,
    while que_heap:
        vertex = heapq.heappop(que_heap)    # vertex is tuple in que_heap list
        adj_weight_dict = adj_dict[vertex[1]] # adj_dict is a dict of dict with weight and neighbour
        for neighbour in adj_weight_dict.keys():
            if relaxation_dict[neighbour] > vertex[0]+ adj_weight_dict[neighbour] and neighbour not in visited:
                parent[neighbour] = vertex[1]
                relaxation_dict[neighbour] = vertex[0] + adj_weight_dict[neighbour]
                heapq.heappush(que_heap,(relaxation_dict[neighbour], neighbour))
                heapq.heapify(que_heap)
        visited.add(vertex[1]) # after visiting all the neighbour of a vertex add that into visited

    # todo - not sure
    if end:
        que = [end] 
        while True:
            if parent[que[-1]] == None:
                break
            else: que.append(parent[que[-1]])
        que.reverse()
        return relaxation_dict, que 
    return relaxation_dict, parent


distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

print(dijkshtra(adj_dict_2,'a'))
print(dijkshtra(adj_dict_2,'a','e'))