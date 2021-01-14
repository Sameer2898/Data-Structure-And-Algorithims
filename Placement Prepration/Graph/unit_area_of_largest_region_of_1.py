import collections
rr = [-1, -1, -1, 0, 0, 1, 1, 1]
cc = [-1, 0, 1, -1, 1, -1, 0, 1]

def isvalid(m, r, c):
    if r < 0 or r >= len(m):
        return False
    if c < 0 or c >= len(m[r]):
        return False
    return True

def find_size(m, row, col):
    q = collections.deque([[row, col]])
    m[row][col] = 2
    ans = 1
    while len(q):
        r = q[0][0]
        c = q[0][1]
        q.popleft()
        for i in range(8):
            nextr = r + rr[i]
            nextc = c + cc[i]
            if isvalid(m, nextr, nextc):
                if m[nextr][nextc] is 1:
                    m[nextr][nextc] = 2
                    q.append([nextr, nextc])
                    ans += 1
    return ans
def findMaxArea(N, M, A):
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] is 1:
                ans = max(ans, find_size(A, i, j))
    return ans

t = int(input('Enter the number of test cases:- '))
for _ in range(t):
    line = input('Enter the number of vertices ans edges:- ').strip().split()
    r=int(line[0])
    c=int(line[1])
    line = input('Enter the elements of the graph:- ').strip().split()
    matrix=[ [0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            matrix[i][j] = int( line[i*c+j] )
    print(findMaxArea(r, c, matrix))