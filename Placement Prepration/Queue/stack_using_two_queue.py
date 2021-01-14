import atexit
import io
import sys

def push(x):
    global queue_1
    global queue_2
    queue_2.append(x)
    while len(queue_1):
        queue_2.append(queue_1[0])
        queue_1.pop(0)
    queue_1, queue_2 = queue_2, queue_1
    
def pop():
    global queue_1
    global queue_2
    if len(queue_1):
        return queue_1.pop(0)
    else:
        return -1

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

queue_1 = [] # first queue
queue_2 = [] # second queue

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n = int(input('Enter the size of the queue:- '))
        a = list(map(int,input('Enter the elements:- ').strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()