def sumMatrix(A,B):
    n1 = len(A)
    n2 = len(B)
    m1 = len(A[0])
    m2 = len(B[0])
    answer = []
    if (n1 == n2 and m1 == m2):
        answer = [[0 for j in range(m1)]  for i in range(n1)]
        for i in range(n1):
            for j in range(m1):
                answer[i][j] = A[i][j] + B[i][j]
    return answer

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):

        n1,m1 = map(int,input('Enter the size of the matrix:- ').strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input('Enter the matrix element:- ').strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                A[i][j]=line1[k]
                k+=1
       
        n2,m2 = map(int,input('Enter the size of the matrix:- ').strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input('Enter the matrix element:- ').strip().split()]
        k=0
        for i in range(n2):
            for j in range (m2):
                B[i][j]=line2[k]
                k+=1

        ans = sumMatrix(A,B)
        if(len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range (len(ans[0])):
                    print(ans[i][j],end=' ')
            print() 