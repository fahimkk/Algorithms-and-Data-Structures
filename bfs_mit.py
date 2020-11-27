from collections import deque

# undirected graph with cycle
adj_dict_1 = {'a':['s','z'],
            's':['a','x'],
            'z':['a'],
            'x':['s','d','c'],
            'd':['x','c','f'],
            'c':['d','x','f','v'],
            'f':['d','c','v'],
            'v':['c','f']}

# directed graph with cycle
adj_dict_2 = {'a':['b','d'],
              'b':['e'],
              'c':['e','f'],
              'd':['b'],
              'e':['d'],
              'f':['f']}
# directed graph without cycle
adj_dict_3 = {'a':['b','g'],
              'b':['c'],
              'c':['d','f'],
              'd':['e','f'],
              'e':['e'],
              'f':['f'],
              'g':['c']}


# bsf by using dque, return all keys in bsf order
def BFS(vertex, adj_dict):
    que_list = deque([vertex])
    check_dict = {vertex:None}
    bsf_list=[vertex]
    while que_list:
        for element in adj_dict[que_list[0]]:
            if element not in check_dict:
                que_list.append(element)
                check_dict[element]=None
                bsf_list.append(element)
        que_list.popleft()
    return bsf_list

#print(BFS('s',adj_dict_1))
# -------------------------------------
# to check whether a graph is cyclic or not
def undirected_BFS_cyclic(vertex, adj_dict):
    que_list = deque([vertex])
    check_dict = {vertex:None}
    bsf_list=[vertex]
    while que_list:
        for element in adj_dict[que_list[0]]:
            if element not in check_dict:
                for elem in adj_dict[element]:
                    if elem in que_list:
                        return True
                que_list.append(element)
                check_dict[element]=None
                bsf_list.append(element)
                
        que_list.popleft()
    return False 

#print('---')
#print(undirected_BFS_cyclic('a',adj_dict_3))
#print('---')


# To find the distance of the element from the vertex
def BSF_mit(vertex,adj_dict):
    level = {vertex:0} # to store the distance of each element  
    parent = {vertex:0} # to check whether the element visited or not
    distance = 1
    frontier = [vertex]
    while frontier:
        next_list = [] # next level distance 
        for element in frontier:
            for adj in adj_dict[element]:
                if adj not in level:
                    level[adj] = distance
                    parent[adj] = element
                    next_list.append(adj)
        frontier = next_list
        distance +=1
    return level, parent
# to find the shortest path of v, take parent[v], parent[parent[v]], etc until s or None
print(BSF_mit('s',adj_dict_1))

class BFSResult:
    def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
    def __init__(self):
        self.adj = {}
    def add_edge(self,u,v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
def bfs(g,s):
    ''' Queue-based implementation of BFS.
    Args:
        g:  a graph with adjacency list adj such that g.adj[u] is list of u's
            neighbours.
        s:  source (vertex)
    '''
    r = BFSResult()
    r.parent = {s:None}
    r.level = {s:0}

    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        for element in g.adj[u]:
            if element not in r.level:
                r.parent[element] = u
                r.level[element] = r.level[u]+1
                queue.append(element)
    return r

graph1 = Graph()
graph1.adj = adj_dict_1
graph2 = Graph()
graph2.add_edge('1','2')
graph2.add_edge('1','5')
graph2.add_edge('2','1')
graph2.add_edge('2','3')
graph2.add_edge('2','4')
graph2.add_edge('2','5')
graph2.add_edge('3','2')
graph2.add_edge('3','4')
graph2.add_edge('4','2')
graph2.add_edge('4','3')
graph2.add_edge('4','5')
graph2.add_edge('5','1')
graph2.add_edge('5','2')
graph2.add_edge('5','4')
#print('----')
#print(graph1.adj)
#print(graph2.adj)
result1 = bfs(graph1,'s') # bfs returns a BFSResult object
result2 = bfs(graph2,'1')
#print(result1.level)
#print(result2.level)
