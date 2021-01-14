import atexit
import io
import sys

def ispar(s):
    stack = []
    for char in s:
        if char in['{', '[', '(']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            return False
    if len(stack):
        return False
    return True

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
        s = str(input('Enter the paracthesis expression:- '))
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")