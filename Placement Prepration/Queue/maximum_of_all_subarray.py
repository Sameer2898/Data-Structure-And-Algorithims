import atexit
import io
import sys
from collections import deque

def max_of_subarrays(arr,n,k):
    ans = []
    d = deque()
    for i in range(k):
        while len(d) and arr[i] >= arr[d[-1]]:
            d.pop()
        d.append(i)
    
    for i in range(k, n):
        ans.append(arr[d[0]])
        while len(d) and d[0] <= i-k:
            d.popleft()
        while len(d) and arr[i] >= arr[d[-1]]:
            d.pop()
        d.append(i)
    ans.append(arr[d[0]])
    d.popleft()
    return ans

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,k = map(int,input('Enter the size of the queue:- ').strip().split())
        arr = list(map(int,input('Enter the elements of the queue:- ').strip().split()))
        res = max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()