import atexit
import io
import sys

def nextGap(gap):
    if(gap <= 1):
        return 0
    return ((gap + 1)//2)

def merge(a,n,b,m):
    gap = n + m
    gap = nextGap(gap)
    while(gap > 0):
        i = 0
        while(i + gap < n):
            if(a[i] > a[i + gap]):
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1
        j = max(0, gap - n)
        
        while(i < n and j < m):
            if(a[i] > b[j]):
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1
        
        if(j < m):
            j = 0
            while(j + gap < m):
                if(b[j] > b[j + gap]):
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1
        gap = nextGap(gap)
    
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == "__main__":
    T = int(input('Enter the number of testcases:- '))
    for tt in range(T):
        n, m = map(int, input('Enter the size of the array:- '))
        a = list(map(int, input('Enter the array elements:-').strip().split()))
        b = list(map(int, input('Enter the array elements:-').strip().split()))
        merge(a, n, b, m)
        if(len(a) != n and len(b) != m):
            print('Do in O(1) space.')
        print(*a, end=' ')
        print(*b)