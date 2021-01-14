import atexit
import io
import sys

def sumOfDigits(n):
    if (n < 10):
        return n
    else:
        return (n%10) + (sumOfDigits(n//10))
    
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        print(sumOfDigits(n))