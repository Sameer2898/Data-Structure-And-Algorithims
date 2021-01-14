import math

def isPrime(N):
    if N == 1:
        return False
    for i in range(2, 1+int(math.sqrt(N))):
        if N % i == 0:
            return False
    return True
    
def exactly3Divisors(N):
    ##Your code here
    N = int(math.sqrt(N))
    count = 0
    for i in range(1, N+1):
        if isPrime(i):
            count += 1
    return count

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        num = int(input('Enter a number:- '))
        print(exactly3Divisors(num))
        T -= 1

if __name__ == "__main__":
    main()