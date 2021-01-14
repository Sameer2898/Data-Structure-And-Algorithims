def transpose(matrix, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for _ in range (t):
        n = int(input('Enter the size of the matirx:- '))
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input('Enter the element of the matrix:- ').strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
    
        transpose(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()