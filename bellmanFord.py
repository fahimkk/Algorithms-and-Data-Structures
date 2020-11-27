import math
# for infinity

# bellman works for -ve weighted graphs also,
# doesn't work for -ve cyclic graph, it returns-
# - undefind. 
# To confirm this we need an extra looping.

def bellman_ford(adj_dict,s):
    # relaxation process are same as that of dijkstra.
    relaxation_dict = {key:math.inf if key != s else 0 for key in adj_dict}
    parent = {s:None}

    # instead of priority que in dijshtra we use adges list,
    # we need a list of all the vertices, the order of the - 
    # -  of the vertex is not important,
    edges = []
    for node, neighbours in adj_dict.items():
        for neighbour in neighbours:
            edges.append((node,neighbour))

    # iterate V-1 times to the graph, for each vertex,
    # for evry i-th iteration i-th vertex became relaxed,

    for _ in range(len(adj_dict_2)):
        for edge in edges:
            # here 1st dict is ajc_dict and 2nd argument is for dict inside it, ie weights
           if relaxation_dict[edge[1]] > relaxation_dict[edge[0]] + adj_dict[edge[0]][edge[1]]: 
               relaxation_dict[edge[1]] = relaxation_dict[edge[0]] + adj_dict[edge[0]][edge[1]]
               parent[edge[1]] = edge[0]
               
    # to confirm no more relaxation, ie no -ve cycle -
    # - do one more for loop to each vertex
    for edge in edges:
        if relaxation_dict[edge[1]] > relaxation_dict[edge[0]] + adj_dict[edge[0]][edge[1]]: 
            raise 'A negative cycle exist.'
    return relaxation_dict

# positive weighted graph
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

# -ve cylic graph
adj_dict_3 ={'a':{'b':1},
             'b':{'c':2},
             'c':{'d':-4,'e':1},
             'd':{'b':1},
             'e':{'e':0}} # here e is the end vertex,
print(bellman_ford(adj_dict_3,'a'))