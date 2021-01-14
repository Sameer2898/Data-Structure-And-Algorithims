import math

def equilibriumPoint(A, N):
    sum = 0
    for i in range(0, N):
        sum += A[i]
    sum2 = 0
    for i in range(0, N, +1):
        sum -= A[i]
        if sum2 == sum:
            return (i + 1)
        sum2 += A[i]
    return -1

def main():
    T = int(input('Enter number of test cases:- '))
    while T > 0:
        N = int(input('Enter the size of array:- '))
        A = [int(x) for x in input('Enter the array element:-').strip().split()]
        print(f'Equilibrium Point is:- {equilibriumPoint(A, N)}')
        T -= 1

if __name__ == "__main__":
    main()
            