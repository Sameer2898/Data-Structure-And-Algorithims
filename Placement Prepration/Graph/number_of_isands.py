import atexit
import io
import sys

def isvalid(x, y, n, m):
    if x < n and  y < m and  x >= 0 and y >= 0:
        return True
    return False
    
def findIslands(A, N, M):
    islands = 0
    stack = []
    dirs = [-1, 0, 1]
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:
                islands += 1
                stack.append([i, j])
                while len(stack):
                    index = stack.pop()
                    ind_x = index[0]
                    ind_y = index[1]
                    a[ind_x][ind_y] = -1
                    for x_dir in dirs:
                        for y_dir in dirs:
                            if isvalid(ind_x + x_dir, ind_y + y_dir, N, M) and a[ind_x + x_dir][ind_y + y_dir] == 1:
                                stack.append([ind_x + x_dir, ind_y + y_dir])
    return islands

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for cases in range(t):
        n,m = map(int,input('Enter the number of vertices ans edges:- ').strip().split())
        cell_info = list(map(int,input('Enter the elements of the graph:- ').strip().split()))
        a = []
        k = 0 # current index
        # create the boolean matrix from cell information
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k+=1
            a.append(row_i)
        print(findIslands(a,n,m))