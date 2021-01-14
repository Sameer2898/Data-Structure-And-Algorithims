import atexit
import io
import sys
import heapq

def kthLargest(a,n,k):
    k_largest = []
    for num in a:
        if len(k_largest) < k:
            heapq.heappush(k_largest, num)
        else:
            curr_min = heapq.heappop(k_largest)
            heapq.heappush(k_largest, max(curr_min, num))
    return heapq.heappop(k_largest)

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
        n, k= map(int, input('Enter the range to find the largest element(seprated by comma):- ').strip().split())
        a = list(map(int, input('Enter the elements of the heap:- ').strip().split()))
        print(kthLargest(a,n,k))