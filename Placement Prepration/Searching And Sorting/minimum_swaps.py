import atexit
import io
import sys

def minSwaps(arr, N):
    pos = []
    for i in range(N):
        pos.append([arr[i], i])
    pos.sort()
    
    visit = [0 for i in range(N)]
    ans = 0
    for i in range(N):
        if (visit[i] or pos[i][1] == i):
            continue
        count = 0
        j = i
        
        while (not visit[j]):
            visit[j] = 1
            j = pos[j][1]
            count += 1
        ans += count - 1
    return ans

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input('Enter number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the array elements:- ').strip().split()))
        print(minSwaps(arr, n))
