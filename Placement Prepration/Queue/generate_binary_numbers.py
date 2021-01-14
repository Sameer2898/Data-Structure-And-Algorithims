import atexit
import io
import sys

def GenerateBinary(n):
    ans = []
    from queue import Queue
    q = Queue()
    q.put('1')
    while n > 0:
        n -= 1
        s1 = q.get()
        ans.append(s1)
        s2 = s1
        q.put(s1 + '0')
        q.put(s2 + '1')
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
        n = int(input('Enter the number:- '))
        res = GenerateBinary(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()