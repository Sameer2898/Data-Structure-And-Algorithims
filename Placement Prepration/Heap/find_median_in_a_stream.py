import atexit
import io
import sys
import heapq
from collections import  defaultdict

def balanceHeaps():
    if abs(len(min_heap) - len(max_heap)) <= 1:
        return 
    if len(min_heap) > len(max_heap):
        value_top = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * value_top)
    else:
        value_top = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, value_top)
    return 
    
def getMedian():
    if len(max_heap) > len(min_heap):
        value = heapq.heappop(max_heap)
        heapq.heappush(max_heap, value)
        return (-1 * value)
    elif len(min_heap) > len(max_heap):
        value = heapq.heappop(min_heap)
        heapq.heappush(min_heap, value)
        return value
    else:
        val_min = heapq.heappop(min_heap)
        val_max = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, val_min)
        heapq.heappush(max_heap, -1 * val_max)
        return ((val_max + val_min) // 2)
        
def insertHeaps(x):
    least_updatehalf = heapq.heappop(min_heap) if len(min_heap) else -1
    
    if least_updatehalf != -1:
        heapq.heappush(min_heap, least_updatehalf)
    
    if x >= least_updatehalf:
        heapq.heappush(min_heap, x)
    else:
        heapq.heappush(max_heap, -1 * x)

min_heap = [] # our min heap to be used for upper half of data.
max_heap = [] # our max heap to be used for lower half of data.

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    
    for _ in range(t):
        n = int(input('Enter the size of the heap:- '))
        for i in range(n):
            insertHeaps(int(input('Enter the elements of the heap:- ')))
            # call this function to balance the two heaps, such that
            # their size does not differ by more than 1.
            balanceHeaps()
            # prints the median
            print(getMedian())