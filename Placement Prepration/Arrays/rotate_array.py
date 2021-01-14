def rotateArray(A, D, N):
    A[0:D] = reversed(A[0:D])
    A[D:N] = reversed(A[D:N])
    A[0:N] = reversed(A[0:N])

def main():
    T = int(input('Enter number of test cases:- '))
    while(T > 0):
        nd = [int(x) for x in input().strip().split()]
        N = nd[0]
        D = nd[1]
        A = [int(x) for x in input().strip().split()]
        rotateArray(A, D, N)
        print('Rotated array is:- ')
        for i in A:
            print(i, end='')
        print()
        T -= 1