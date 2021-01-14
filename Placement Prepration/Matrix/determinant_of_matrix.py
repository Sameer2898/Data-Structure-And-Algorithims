def getcofactor(matrix, temp, p, q, n):
    i, j = 0, 0
    for row in range(n):
        for column in range(n):
            if row != p and column != q:
                temp[i][j] = matrix[row][column]
                j += 1
                if j == n - 1:
                    j = 0
                    i += 1

def determinantOfMatrix(matrix,n):
    d = 0
    if n == 1:
        return matrix[0][0]
    temp = [[0 for i in range(n)] for i in range(n)]
    sign = 1
    for i in range(n):
        getcofactor(matrix, temp, 0, i, n)
        d += sign * matrix[0][i] * determinantOfMatrix(temp, n - 1)
        sign = -sign
    return d

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter the size of the matrix:- '))
        values = list(map(int, input('Enter the elementes of the matrix:- ').strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        print(determinantOfMatrix(matrix,n))