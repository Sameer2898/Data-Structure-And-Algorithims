import atexit
import io
import sys

def strstr(s,p):
    s_index = 0
    while s_index < len(s):
        if s[s_index] == p[0]:
            p_index = 0
            temp_s = s_index
            while temp_s < len(s) and s[temp_s] == p[p_index]:
                p_index += 1
                temp_s += 1
                if p_index == len(p):
                    return s_index
        s_index += 1
    return -1

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input('Enter the number of test cases:- '))
    for cases in range(t):
        s,p =input('Enter the string and the pattern to find in the string:- ').strip().split()
        print(strstr(s,p))