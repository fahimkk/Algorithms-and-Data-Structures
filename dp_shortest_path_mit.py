import math
# for topological_sort

# Shortest path for DAG(directed acyclic graph)
# using memorized dp algorithm

class Graph:
    def __init__(self):
        self.adj = {}
    def add_edge(self,u,v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    def itervertices(self):
        return self.adj.keys() 
    def neighbours(self, v):
        return self.adj[v]
    def num_vertices(self):
        return len(self.adj)
    def inverse_neighbours(self,s):
        self.revers_dict = {}
        for vertex, neighbours_dict in self.adj.items():
            for neighbour, weight in neighbours_dict.items():
                if neighbour not in self.revers_dict:
                    self.revers_dict[neighbour] = {vertex:weight} 
                else:
                # to avoid last vertex mapping towards itself
                    if  neighbour== vertex and weight ==0:
                        continue
                    self.revers_dict[neighbour][vertex] = weight

        # to map the source vertex to itself.
        for vertex in self.adj:
            if vertex not in self.revers_dict:
                self.revers_dict[vertex] = {vertex:0}
        return self.revers_dict[s]

    def weight(self,u,v):
        return self.adj[u][v]

class ShortestPathResult(object):
    def __init__(self):
        # d dictionary, key-vertex, value- shortest path
        self.d = {}  
        self.parent = {}

# In dikjstra method, we select the min wighted vertex for the
# next iteration, here select a vertex and find its inverse neighbours
# and find the shortest path from it, and make that node as parent.

# sp_dp is used the function shotest_path below
def sp_dp(graph, v,result):
    ''' Recursion on finding the shortest path to v.
    Args:
        graph: weighted DAG.
        v: a vertex in graph.
        result: for memoization and keeping track 
                of the result '''
    if v in result.d:
        return result.d[v]
    result.d[v] = math.inf
    result.parent[v] = None
    for u in graph.inverse_neighbours(v):
        new_distance = sp_dp(graph,u,result) + graph.weight(u,v)
        if new_distance < result.d[v]:
            result.d[v] = new_distance
            result.parent[v] = u
    return result.d[v]

def shortest_path(graph, s):
    '''Single source shortest path using dp on a DAG
    Args:
        graph: weighted DAG.
        s: source '''
    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s]=None
    for v in graph.itervertices():
        sp_dp(graph,v,result)
    return result

def shortest_path_bottomup(graph, s):
    '''Bottom-up DP for finding single source shortest
    paths on a DAG.
    Args: 
        graph: weight DAG
        s:source '''
    order = dfs_mit.topological_sort(graph)
    result = ShortestPathResult()
    for v in graph.itervertices():
        result.d[v] = float('int')
        result.parent[v] = None
    result.d[s] = 0
    for v in order:
        for w in graph.neighbours(v):
            new_distance=result.d[v] + graph.weight(w,v)
            if result.d[w]> new_distance:
                result.d[w] = new_distance
                result.parent[w] = v
    return result

# cyclic grpah
def shortest_path_cycle(graph,s):
    '''Single source shortest paths using DP on a graph
    with cycles but no negative cycles.
    Args:
        graph: weighted graph with no negative cycles.
        s: source '''
    result = ShortestPathResult()
    num_vertices = graph.num_vertices()
    for i in range(num_vertices):    
        result.d[(i,s)] = 0
        result.parent[(i,s)] = None
    for v in graph.itervertices():
        if v is not s:
            result.d[(0,v)] = math.inf
    for v in graph.itervertices():
        sp_cycle_dp(graph, num_vertices-1,v,result)
    
    d={}
    parent={}
    for v in graph.itervertices():
        d[v]= result.d[(num_vertices-1, v)]
        parent[v] = result.parent[(num_vertices-1,v)]
    result.d, result.parent = d, parent
    return result

def sp_cycle_dp(graph,k,v,result):
    '''Recursion on finding the shortest path to v with
    no more than k edges on graph with cycles.
    Args:
        graph: weighted graph,
        k: kth level subproblem, i.e. finding paths with 
            no more than k edges.
        v: a vertex in the graph
        result: for memoization and keeping track of the result.
    '''
    if (k,v) in result.d:
        return result.d[(k,v)]
    result.d[(k,v)] = math.inf
    result.parent[(k,v)] = None
    for u in graph.inverse_neighbours(v):
        new_distance = sp_cycle_dp(graph,k-1,u,result)+graph.weight(u,v)
        if new_distance < result.d[(k,v)]:
            result.d[(k,v)] = new_distance
            result.parent[(k,v)] = u
    return result.d[(k,v)]


# directed graph with cycle
adj_dict_2 = {'s':{'a':2,'b':4},
              'a':{'a':0},
              'b':{'c':4},
              'c':{'e':1,'d':2},
              'd':{'e':2,'b':-3},
              'e':{'e':0}}



# directed graph without cycle
adj_dict_3 = {'a':{'b':10,'g':3},
              'b':{'c':2},
              'g':{'c':4},
              'c':{'d':4,'f':8},
              'd':{'e':7,'f':4},
              'e':{'e':0},
              'f':{'f':0}}

# directed graph with cycle
adj_dict_4 = {'s':{'a':1,'b':2},
              'a':{'e':2,'c':5,'b':3},
              'b':{'c':3,'a':1,'d':1},
              'c':{'e':3},
              'd':{'c':2,'f':1},
              'e':{'f':4,'d':1},
              'f':{'b':2}}

graph = Graph()
graph.adj = adj_dict_2
sp = shortest_path(graph,'s')
sp_cycle = shortest_path_cycle(graph,'s')
print(sp.parent)
print(sp.d)
print('---')
print(sp_cycle.parent)
print(sp_cycle.d)
