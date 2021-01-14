import atexit
import io
import sys
import heapq
from collections import  defaultdict

def nearlySorted(a,n,k):
    min_heap = []
    ans = []
    for num in a:
        if len(min_heap) < 2 * k:
            heapq.heappush(min_heap, num)
        else:
            ans.append(heapq.heappop(min_heap))
            heapq.heappush(min_heap, num)
    while(len(min_heap)):
        ans.append(heapq.heappop(min_heap))
    return ans

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,k = map(int,input('Enter the size of the list and the element:- ').strip().split())
        a = list(map(int,input('Enter the elements of the heap:- ').strip().split()))
        print(*nearlySorted(a,n,k))