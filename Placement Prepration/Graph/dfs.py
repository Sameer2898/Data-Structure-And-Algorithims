import atexit
import io
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs_util(g, root, vis, ans):
    ans.append(root)
    vis[root] = True
    for nodes in g[root]:
        if not vis[nodes]:
            dfs_util(g, nodes, vis, ans)
    return

def dfs(g,N):
    vis = [False for i in range(N)]
    ans = []
    dfs_util(g, 0, vis, ans)
    return ans

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        N,E = map(int,input('Enter the number of vertices ans edges:- ').strip().split())
        g = Graph(N)
        edges = list(map(int,input('Enter the elements of a graph:- ').strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)

        res = dfs(g.graph,N)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()