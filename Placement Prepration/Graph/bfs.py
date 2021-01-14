import atexit
import io
import sys
from collections import defaultdict
import queue

def bfs(g,N):
    ans = []
    q = queue.Queue()
    vis = [False for i in range(N)]
    q.put(0)
    while(not q.empty()):
        node = q.get()
        vis[node] = True
        ans.append(node)
        for nodes in g[node]:
            if not vis[nodes]:
                q.put(nodes)
                vis[nodes] = True
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
        edges = list(map(int,input('Enter the elements of the graph:- ').strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add a directed edge from u to v

        res = bfs(g.graph,N) # print bfs of graph
        for i in range (len (res)):
            print (res[i], end = " ")
        print()