
visited = set()
def dfs_simple(visited,adj_dict,node):
    visited.add(node)
    for neighbour in  adj_dict[node]:
        if neighbour not in visited:
            dfs_simple(visited,adj_dict,neighbour)

#dfs_simple(visited,adj_dict_2,'a')
#print(visited)
# ----------------------------

def dfs_visited(parent,adj_dict,node):
    for neighbour in adj_dict[node]:
        if neighbour not in parent:
            parent[neighbour] = node
            dfs_visited(parent,adj_dict,neighbour)

def dfs(adj_dict):
    vertex = adj_dict.keys()
    parent={}
    for node in vertex:
        if node not in parent:
            parent[node] = None
            dfs_visited(parent,adj_dict, node)
    return parent        
#print(dfs(adj_dict_3))
# -------------------------------

def dfs_visited_topo(parent,adj_dict,node,dfs_list):
    for neighbour in adj_dict[node]:
        if neighbour not in parent:
            parent[neighbour] = node
            dfs_visited_topo(parent,adj_dict,neighbour,dfs_list)
    dfs_list.append(node)

def dfs_topo(adj_dict):
    vertex = adj_dict.keys()
    dfs_list = []
    parent={}
    for node in vertex:
        if node not in parent:
            parent[node] = None
            dfs_visited_topo(parent,adj_dict, node, dfs_list)
        dfs_list.reverse()  # dfs_visit will add only the last element in recursion
    return parent, dfs_list

#print(dfs_topo(adj_dict_3))
# ---------------------------------

# Mit 
class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {} # Edge classification for direction
        self.order = []
        self.t = 0
class Graph:
    def __init__(self):
        self.adj = {}
    def add_edge(self,u,v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    def itervertices(self):
        return self.adj.keys()
    def neighbour(self,v):
        return self.adj[v]

def dfs_visit(g,v,result,parent=None):
    result.parent[v] = parent 
    result.t +=1
    result.start_time[v] = result.t
    if parent:
        result.edges[(parent, v)] = 'tree'
    for n in g.neighbour(v):
        if n not in result.parent: # n is not visited
            dfs_visit(g,n,result,v)
        elif n not in result.finish_time:
            result.edges[(v,n)] = 'back'
        elif result.start_time[v] < result.start_time[n]:
            result.edges[(v,n)] = 'forward'
        else:
            result.edges[(v,n)] = 'cross'
    result.t +=1
    result.finish_time[v] = result.t
    result.order.append(v)



def dfs_mit(g):
    result = DFSResult()
    for vertex in g.itervertices():
        if vertex not in result.parent:
            dfs_visit(g,vertex,result)
    return result


def topological_sort(g):
    dfs_result = dfs_mit(g)
    dfs_result.order.reverse()
    return dfs_result.order
#print(topological_sort(graph))
# ------------------------------------

# TODO
# cyclic or not , by using flag -1, 0, 1
# -1 for unvisited, 0 - for visited and in the stack
# 1 for visted and poped out from stack

# return true if the graph contains cycle
def directed_dfs_cyclic(adj_dict, node):
    stack = [node]
    path = []
    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.append(node)
        for neighbour in adj_dict[node]:
            if neighbour in stack:
                return True 
            stack.append(neighbour)
    return False 
  
# to work this without inputing node, we have to goes through 
# each vertex, becouse in directed graph if a node is missed 
# then its cyclicity may loss.

#print(directed_dfs_cyclic(adj_dict_2,'a'))

# to find the topologiclal order we have to find the indegree
# pop the node with indegree zero

def find_indegree(adj_dict):
    indegree_list = {} 
    for key in adj_dict:
        count = 0
        for i in adj_dict.values():
            if key in i :
                count +=1
        if count in indegree_list:
            indegree_list[count].append(key)
        else: indegree_list[count]=[key]
    return indegree_list

def topological_order(adj_dict):
    import copy
    copy_adj_dict = copy.copy(adj_dict) 
    # this for loop is for, in graph at the end element is 
    # connected to itself.
    for key,value in copy_adj_dict.items():
        if [key] == value:
            copy_adj_dict[key] = [0]
    topo_list = []
    for i in range(len(adj_dict)):
        in_degree_dict = find_indegree(copy_adj_dict)
        if 0 in in_degree_dict:
            element = in_degree_dict[0].pop()
            topo_list.append(element)
            del copy_adj_dict[element]
    return topo_list


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


graph = Graph()
graph.adj = adj_dict_3
mit = dfs_mit(graph)
#print(mit)
#print(mit.parent)
#print(mit.edges)
#print(mit.order)

print(topological_order(adj_dict_3))
