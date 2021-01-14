import atexit
import io
import sys

def printMaxOfMin(arr,n):
    stack = []
    left = [-1 for i in range(n)]
    right = [n for i in range(n)]
    for i in range(n):
        while len(stack) and a[stack[-1]] >= a[i]:
            stack.pop()
        if len(stack):
            left[i] = stack[-1]
        stack.append(i)
    
    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) and a[stack[-1]] >= a[i]:
            stack.pop()
        if len(stack):
            right[i] = stack[-1]
        stack.append(i)
    
    ans = [0 for i in range(n+1)]
    for i in range(n):
        length = right[i] - left[i] - 1
        ans[length] = max(ans[length], a[i])
        
    for i in range(n-1, -1, -1):
        ans[i] = max(ans[i], ans[i + 1])
    
    return ans[1:]

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
        n = int(input('Enter the size of the array:- '))
        a = list(map(int,input('Enter the elements of the array:- ').strip().split()))
        res = printMaxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()