
import atexit
import io
import sys

def isAnagram(a,b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    if a_sorted == b_sorted:
        return True
    else:
        return False

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        a,b=map(str,input('Enter the two strings seprated by space:- ').strip().split())
        if(isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 