def multiplyMatrix(A,B):
    n1 = len(A)
    n2 = len(B)
    m1 = len(A[0])
    m2 = len(B[0])
    answer = []
    if (m1 == n2):
        answer = [[0 for j in range(m2)]  for i in range(n1)]
        for i in range(n1):
            for j in range(m2):
                sum = 0
                for k in range(0, m1):
                    sum += A[i][k] * B[k][j]
                answer[i][j] = sum
    return answer

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):

        n1,m1 = map(int,input('Enter the size of matrix:- ').strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input('Enter the matrix element:- ').strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                A[i][j]=line1[k]
                k+=1
       
        n2,m2 = map(int,input('Enter the sizeof matrix:- ').strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input('Enter the matrix element:- ').strip().split()]
        k=0
        for i in range(n2):
            for j in range (m2):
                B[i][j]=line2[k]
                k+=1

        ans = multiplyMatrix(A,B)

        if(len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range (len(ans[0])):
                    print(ans[i][j],end=' ')
            print()