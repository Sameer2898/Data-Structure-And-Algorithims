import atexit
import io
import sys

def getMaxOccurringChar(s):
    occurences = [0 for i in range(256)]
    for char in s:
        occurences[ord(char)] += 1
    max_occurences = 0
    character = '~'
    for i in range(256):
        if (occurences[i] > max_occurences):
            character= chr(i)
            max_occurences = occurences[i]
    return character

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
        s=str(input('Enter the input:- '))
        print(getMaxOccurringChar(s))