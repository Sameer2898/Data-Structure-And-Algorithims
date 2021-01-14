def spirallyTraverse(matrix, r, c): 
    row = 0
    col = 0
    answer = []
    while row < r and col < c:
        for i in range(col, c):
            answer.append(matrix[row][i])
        row += 1
        
        for i in range(row, r):
            answer.append(matrix[i][c - 1])
        c -= 1
        
        if row < r:
            for i in range(c - 1, col - 1, -1):
                answer.append(matrix[r - 1][i])
            r -= 1
        
        if col < c:
            for i in range(r - 1, row - 1, -1):
                answer.append(matrix[i][col])
            col += 1        
    return answer

if __name__ == '__main__':
    t = int(input('enter the number of test cases:- '))
    for _ in range(t):
        r,c = map(int, input('Enter the size of the matrix:- ').strip().split())
        values = list(map(int, input('Enter the elements:- ').strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        ans = spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

