from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def findDistance(matrix,m,n):
    ans = [[-1 for _ in range(n)] for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'G':
                ans[i][j] = 0
                q.append((i, j))
    while len(q):
        r = q[0][0]
        c = q[0][1]
        q.popleft()
        for i in range(4):
            nextr = r + dr[i]
            nextc = c + dc[i]
            if nextr >= 0 and nextr < m and nextc >= 0 and nextc < n:
                if ans[nextr][nextc] == -1 and matrix[nextr][nextc] == 'O':
                    ans[nextr][nextc] = ans[r][c] + 1
                    q.append((nextr, nextc))
    return ans

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        size = input('Enter the vertices and edges of the graph:- ').strip().split()
        m = int(size[0])
        n = int(size[1])
        matrix=[]
        for _ in range(m):
            matrix.append( [ x for x in input('Enter the elements of a graph:- ').strip().split() ] )
        result=findDistance(matrix,m,n)
        
        for i in result:
            for j in i:
                print(j, end=' ')
            print()