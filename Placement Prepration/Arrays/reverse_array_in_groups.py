import math

def reverseInGroups(A,N,K):
    #Your code here
    i = 0
    while(i<N):
        if(i+K<N):
            A[i:i+K] = reversed(A[i:i+K])
            i += K
        else:
            A[i:] = reversed(A[i:])
            i += K
    return A

def main():
    t = int(input('Enter the number of test cases:- '))
    while(t > 0):
        nk = [int(x) for x in input().strip().split()]
        N = nk[0]
        K = nk[1]
        A = [int(x) for x in input().strip().split()]
        A = reverseInGroups(A, N, K)
        for i in A:
            print(f'After reverse the array is:- {i}')
        print()
        t -= 1

if __name__ == "__main__":
    main()