import atexit
import io
import sys
from collections import defaultdict

def areIsomorphic(s,p):
    d = defaultdict(chr)
    if (len(s) != len(p)):
        return False
    marked = [0 for i in range(26)]
    
    for i in range(len(s)):
        c = s[i]
        c_p = p[i]
        if (c not in d):
            if (marked[ord(c_p) - ord('a')]):
                return False
            else:
                marked[ord(c_p) - ord('a')] = 1
                d[c] = c_p
        else:
            if (d[c] != c_p):
                return False
    return True

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
        s = input('Enter the first string:-')
        p = input('Enter the second string:- ')
        if(areIsomorphic(s,p)):
            print(1)
        else:
            print(0)