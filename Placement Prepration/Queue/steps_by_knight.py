import sys
sys.setrecursionlimit(10**6)

class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
    
def is_inside(x, y, n):
    if x >= 1 and x <= n and y >= 1 and y <= n:
        return True
    return False

def minStepToReachTarget(knightpos, targetpos, n):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    queue.append(cell(knightpos[0], knightpos[1], 0))
    visited = [[False for i in range(n  + 1)] for j in range(n + 1)]
    visited[knightpos[0]][knightpos[1]] = True
    while (len(queue) > 0):
        t = queue[0]
        queue.pop(0)
        if t.x == targetpos[0] and t.y == targetpos[1]:
            return t.dist
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if is_inside(x, y, n) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        size = int(input('Enter the size of the board:- '))
        knightpos = tuple(map(int, input('Enter the knight current position:- ').strip().split(' ')))  #source
        targetpos = tuple(map(int, input('Enter the target position of the knight:- ').strip().split(' ')))   #destination
        print(minStepToReachTarget(knightpos, targetpos, size))