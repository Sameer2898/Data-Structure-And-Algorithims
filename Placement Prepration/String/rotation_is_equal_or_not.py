import atexit
import io
import sys

def areRotations(s1,s2):
    s = s1+s1
    if len(s1) == len(s2) and s2 in s:
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
        s1 = input('Enter the first string:-')
        s2 = input('Enter the second string:-')
        if(areRotations(s1,s2)):
            print(1)
        else:
            print(0)