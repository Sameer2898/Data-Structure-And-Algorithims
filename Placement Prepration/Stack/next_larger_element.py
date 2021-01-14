import atexit
import io
import sys

def createstack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) == 0

def push(stack, s):
    stack.append(s)

def pop(stack):
    if isempty(stack):
        print('Error : stack underflow')
    else:
        return stack.pop()

def nextLargerElement(arr,n):
    next_greater = [-1 for i in range(n)]
    s = createstack()
    element = 0
    next = 0
    push(s, [arr[0],0])
    for i in range(1, n, 1):
        next = arr[i]
        if isempty(s) == False:
            elem = pop(s)
            element = elem[0]
            curr_index = elem[1]
            while element < next:
                next_greater[curr_index] = next
                if isempty(s) == True:
                    break
                elem = pop(s)
                element = elem[0]
                curr_index = elem[1]
            if element > next:
                push(s, [element, curr_index])
        push(s, [next, i])
    return next_greater

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
        n = int(input('Enter the size of the list:- '))

        a = list(map(int,input('Enter the elements:- ').strip().split()))
        res = n