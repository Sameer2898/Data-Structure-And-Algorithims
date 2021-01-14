
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(v, visit, graph, s):
    visit[v] = True
    for i in graph[v]:
        if visit[i] == False:
            dfs(i, visit, graph, s)
    s.append(v)
    
def topoSort(n, adj):
    visit = [False] * n
    s = []
    for i in range(n):
        if visit[i] is False:
            dfs(i, visit, graph, s)
    return s[::-1]

def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        e,N = list(map(int, input('Enter the number of vertices ans edges:- ').strip().split()))
        arr = list(map(int, input('Enter the elements of the graph:- ').strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        
        if check(graph, N, res):
            print(1)
        else:
            print(0)