def convertToWave(A,N):
    i = 0
    while i < N-1:
        temp = A[i]
        A[i] = A[i + 1]
        A[i + 1] = temp
        i += 2

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        N = int(input('Enter how many elements you want to store in array:- '))
        A = [int(i) for i in input('Enter the array elements:- ').strip().split()]
        convertToWave(A, N)
        for i in A:
            print(i, end=' ')
        print()
        T -= 1

if __name__ == "__main__":
    main()