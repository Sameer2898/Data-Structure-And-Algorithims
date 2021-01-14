import atexit
import io
import sys

def calculateSpan(a,n):
    S = [0 for i in range(n + 1)]
    st = []
    st.append(0)
    S[0] = 1
    for i in range(1, n):
        while (len(st) > 0 and a[st[-1]] <= a[i]):
            st.pop()
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
        st.append(i)
    return S[0:n]

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
        n = int(input('Enter the size of the array:- '))
        a = list(map(int,input('Enter the elements of the array:- ').strip().split()))
        print(*calculateSpan(a, n)) 