def transpose(matrix, n): 
    r, c = n, n
    for i in range(r):
        for j in range(i, c):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t

def reverse(matrix, n):
    c = n
    r = n
    for i in range(c):
        j = 0
        k = c - 1
        while j < k:
            t = matrix[j][i]
            matrix[j][i] = matrix[k][i]
            matrix[k][i] = t
            j += 1
            k -= 1

def rotateby90(a, n):
    transpose(a, n)
    reverse(a, n)

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for _ in range (t):
        n = int(input('Enter the size of matrix'))
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input('Enter the elements:- ').strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
    
        rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()