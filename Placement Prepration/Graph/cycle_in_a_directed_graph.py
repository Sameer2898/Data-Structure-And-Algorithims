from collections import defaultdict

def dfs_util(v, ans, visit, graph):
    if visit[v] is False:
        visit[v] = True
        ans[v] = True
        for i in graph[v]:
            if not visit[i] and dfs_util(i, ans, visit, graph):
                return True
            elif ans[i]:
                return True
    ans[v] = False
    return False
    
def isCyclic(n, graph):
    visit = [False] * n
    ans = [False] * n
    for i in range(n):
        if visit[i] == False:
            if dfs_util(i, ans, visit, graph) is True:
                return True
    return False

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n,e = list(map(int, input('Enter the number of vertices ans edges:- ').strip().split()))
        arr = list(map(int, input('Enter the elements of the graph:- ').strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)