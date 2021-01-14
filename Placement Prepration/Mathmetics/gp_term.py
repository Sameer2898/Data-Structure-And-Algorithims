import math

def termOfGP(A,B,N):
    r = B/A
    return A * pow(r, N-1)

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        AB = [int(i) for i in input().strip().split()]
        A = AB[0]
        B = AB[1]
        num = int(input())
        # print(f'The nth value of {num} is:- {math.floor(termOfGP(A, B, num))}')
        print(math.floor(termOfGP(A, B, num)))
        T -= 1

if __name__ == "__main__":
    main()