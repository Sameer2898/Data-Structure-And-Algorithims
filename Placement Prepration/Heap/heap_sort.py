import atexit
import io
import sys

def heapify(arr, n, i):
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n  and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def buildHeap(arr,n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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
        arr = list(map(int, input('Enter the element of the heap:- ').strip().split()))
        buildHeap(arr,n)
        print(*arr)