import atexit
import io
import sys

def sortByFreq(a,n):
    freq = [0 for i in range(max(a) + 1)]
    hash_for_freq = [[] for i in range(n + 1)]
    for num in a:
        freq[num] += 1
    for i in range(max(a) + 1):
        if freq[i]:
            hash_for_freq[freq[i]].append(i)
            
    l = []
    for i in range(n, 0, -1):
        for num in hash_for_freq[i]:
            for j in range(i):
                l.append(num)
    return l

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for tt in range(t):
        n = int(input('Enter the size of the array:- '))
        a = list(map(int, input('Enter the elements of the array:- ').strip().split()))
        l = sortByFreq(a,n)
        print(*l)