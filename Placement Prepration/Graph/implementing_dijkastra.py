def minDistance(dist, sptSet, V):
    min = 1000005
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(src, V, graph):
    dist = [1000005] *V
    dist[src] = 0
    sptSet = [False] * V
    for cout in range(V):
        u = minDistance(dist, sptSet, V)
        sptSet[u] = True
        for v in range(V):
            if graph[u][v] > 0 and sptSet[v] == False and \
            dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
    return dist

def printSolution(dist, V):
    for node in range(V):
        print(dist[node] , end=" ")
    print()


if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for tst in range(t):
        v = int(input('Enter the size of the graph:- '))
        graph = [[0 for column in range(v)]
                    for row in range(v)]

        lst = [int(x) for x in input('Enter the elements of the graph:- ').strip().split()]
        k=0
        for i in range(v):
            for j in range(v):
                graph[i][j] = lst[k]
                k+=1
        s = int(input())
        res = dijkstra(s, v, graph)
        
        printSolution (res, v)