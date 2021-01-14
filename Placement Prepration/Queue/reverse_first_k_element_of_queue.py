import atexit
import io
import sys

def reverseK(queue,k,n):
    stack = []
    ansqueue = []
    for i in range(k):
        stack.append(queue.pop(0))
    while len(stack):
        ansqueue.insert(0, stack.pop(0))
    while len(queue):
        ansqueue.append(queue.pop(0))
    return ansqueue

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
        a = list(map(int,input('Enter the element to the queue:- ').strip().split()))
        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*reverseK(queue,k,n))