import atexit
import io
import sys

def power_set(s, index=0, curr=''):
    n = len(s)
    if index == n:
        powerSet.ans.append(curr)
        return
    power_set(s, index+1, curr)
    power_set(s, index+1, curr+s[index])

def powerSet(s):
    powerSet.ans = []
    power_set(s)
    return powerSet.ans

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
        s = str(input('Enter a string:- '))
        ans = powerSet(s)
        ans.sort()
        print(*ans)