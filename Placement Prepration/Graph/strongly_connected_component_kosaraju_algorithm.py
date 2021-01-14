def DFS (graph, i, V, vis):
    if (vis[i] == True):
        return
    vis[i] = True
    for j in graph[i]:
        DFS (graph, j, V, vis)    

def Transpose (graph, V):
    g = defaultdict(list)
    for i in range (V):
        for j in graph[i]:
            g[j].append(i)
    return g

def fillStack (graph, V, i, vis, stack):
    if vis[i] == True:
        return
    vis[i] = True
    for j in graph[i]:
        if (vis[j] == False):
            fillStack (graph, V, j, vis, stack)
    stack.append (i)

def countSCCs (graph, V):
    stack = []
    vis = [False]*V
    for i in range (V):
        if (vis[i] == False):
            fillStack (graph, V, i, vis, stack)
    tp = Transpose (graph, V)    
    for i in range (V):
        vis[i] = False
    cnt = 0
    while stack:
        i = stack.pop()
        if vis[i] == False:
            DFS (tp, i, V, vis)
            cnt += 1
    return cnt

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n,e = list(map(int, input('Enter the number of vertices ans edges:- ').strip().split()))
        arr = list(map(int, input('Enter the elements of the graph:- ').strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print (countSCCs(graph, n))