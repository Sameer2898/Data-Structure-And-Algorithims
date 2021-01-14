import atexit
import io
import sys
import heapq
from collections import  defaultdict

def kMostFrequent(a,n,k):
    freq = defaultdict(int)
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    min_heap = []
    
    for key in freq:
        num = freq[key]
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            curr_min = heapq.heappop(min_heap)
            heapq.heappush(min_heap, max(curr_min, num))
    return sum(min_heap)

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
        n = int(input('Enter the size of the heap:- '))
        a = list(map(int, input('Enter the elements of the heap:- ').strip().split()))
        k = int(input('Enter the number to find the most occuring element:- '))
        print(kMostFrequent(a,n,k))