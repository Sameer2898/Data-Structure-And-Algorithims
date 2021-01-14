def Kclosest(arr, n, x, k):
    max_heap = [(-1 * abs(x - arr[i]), -1 * arr[i]) for i in range(k)]
    heapq.heapify(max_heap)
    for i in range(k, n):
        dist = -1 * max_heap[0][0]
        hno = -1 * max_heap[0][1]
        if abs(arr[i] - x) < dist or (abs(arr[i] - x) == dist and arr[i] < hno):
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-1 * abs(x - arr[i]), -1 * arr[i]))
    ans = [-1 * x[1] for x in max_heap]
    ans.sort()
    return ans

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        line = input('Enter the three values:- ').strip().split()
        n = int( line[0] )
        x = int( line[1] )
        k = int( line[2] )
        arr = [int(x) for x in input('Enter the elements of the graph:- ').strip().split()]
        result=Kclosest(arr, n, x, k)
        for i in result:
            print(i, end=' ')
        print()