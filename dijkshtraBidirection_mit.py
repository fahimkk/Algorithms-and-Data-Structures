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

adj_dict_3 = {'s':{'u':3,'w':5},
              'u':{'v':3},
              'w':{'t':5},
              'v':{'t':3},
              't':{'t':0}}

def dijkshtra(adj_dict, s,end=False):
    que_heap_f = [(0,s)] # forward heap
    que_heap_b = [(0,end)] # backword heap

    relaxation_dict = {key:math.inf if key !=s else 0 for key in adj_dict}
    relaxation_dict_b = {key:math.inf if key !=end else 0 for key in adj_dict}

    # instead of below code, to reverse graph we can use
    # code from dp_shortest_path_mit.py - inverse_neighbours method.
    # to reverse the path.
    revers_dict = {s:{s:0}}
    for key, value in adj_dict.items():
        for k in value:
            if k not in revers_dict:
                revers_dict[k] = {key:value[k]}
            else: revers_dict[k][key] = value[k]
    if revers_dict[end][end]==0: del revers_dict[end][end]

    visited = set()
    visited_b = set()
    parent={s:None} # not neccessary,
    parent_b={end:None} 
    vert = ''
    while que_heap_f and que_heap_b:
        vertex = heapq.heappop(que_heap_f)    # vertex is tuple in que_heap list
        vertex_b = heapq.heappop(que_heap_b)    # vertex is tuple in que_heap list
        if vertex == vertex_b:
            vert = vertex
            break
        adj_weight_dict = adj_dict[vertex[1]] # adj_dict is a dict of dict with weight and neighbour
        for neighbour in adj_weight_dict.keys():
            if relaxation_dict[neighbour] > vertex[0]+ adj_weight_dict[neighbour] and neighbour not in visited:
                parent[neighbour] = vertex[1]
                relaxation_dict[neighbour] = vertex[0] + adj_weight_dict[neighbour]
                heapq.heappush(que_heap_f,(relaxation_dict[neighbour], neighbour))
                heapq.heapify(que_heap_f)
        visited.add(vertex[1]) # after visiting all the neighbour of a vertex add that into visited

        adj_weight_dict_b = revers_dict[vertex_b[1]] # adj_dict is a dict of dict with weight and neighbour
        for neighbour in adj_weight_dict_b.keys():
            if relaxation_dict_b[neighbour] > vertex_b[0]+ adj_weight_dict_b[neighbour] and neighbour not in visited:
                parent_b[neighbour] = vertex_b[1]
                relaxation_dict_b[neighbour] = vertex_b[0] + adj_weight_dict_b[neighbour]
                heapq.heappush(que_heap_b,(relaxation_dict_b[neighbour], neighbour))
                heapq.heapify(que_heap_b)
        visited_b.add(vertex_b[1]) # after visiting all the neighbour of a vertex add that into visited

    # to find the minimum distance of possible paths 
    min_path = []
    for key in parent: # first for loop in forward, so max element is in parent
        value = relaxation_dict[key] + relaxation_dict_b[key]
        if value != math.inf:
            heapq.heappush(min_path,(key,value))
    target = heapq.heappop(min_path)

    # to get the path 
    que = [target[0]] 
    while True:
        if parent[que[-1]] == None:
            break
        else: que.append(parent[que[-1]])
    que.reverse()
    # for the backword parent, 
    while True:
        if parent_b[que[-1]] == None:
            break
        else: que.append(parent_b[que[-1]])
    return que


print(dijkshtra(adj_dict_3,'s','t'))