import atexit
import io
import sys
import heapq
from collections import  defaultdict

def minCost(a,n):
    min_heap = []
    for num in a:
        heapq.heappush(min_heap, num)
    total_cost = 0
    while(len(min_heap) > 1):
        val_1 = heapq.heappop(min_heap)
        val_2 = heapq.heappop(min_heap)
        val = val_1 + val_2
        total_cost += val
        heapq.heappush(min_heap, val)
    return total_cost

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        n = int(input('Enter the number of elements in the heap:- '))
        a = list(map(int, input().strip('Enter the elements of heap:- ').split()))
        print(minCost(a,n))