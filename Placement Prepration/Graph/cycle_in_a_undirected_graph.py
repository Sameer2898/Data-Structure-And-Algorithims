import atexit
import io
import sys
from collections import defaultdict

def dfs(g, node, parent, vis):
    vis[node] = 1
    for nodes in g[node]:
        if not vis[nodes]:
            if dfs(g, nodes, node, vis):
                return 1
        else:
            if nodes != parent:
                return 1
    return 0
    
def isCyclic(g,n):
    vis = [0 for i in range(n)]
    for node in range(n):
        if vis[node] == 0:
            if dfs(g, node, -1, vis):
                return 1
    return 0

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input('Enter the nomber of test cases:- '))
    for cases in range(test_cases) :
        N,E = map(int,input('Enter the number of vertices ans edges:- ').strip().split())
        g = Graph(N)
        edges = list(map(int,input('Enter the elements of the graph:- ').strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))