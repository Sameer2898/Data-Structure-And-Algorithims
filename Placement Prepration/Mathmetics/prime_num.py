def isPrime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if (N % 2 == 0 or N % 3 == 0):
        return False

    i = 5
    while(i * i <= N):
        if (N % i == 0 or N % (i + 2) == 0):
            return False
        i += 6
    return True
    
def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        num = int(input('Enter a number:- '))
        if isPrime(num):
            print('Yes')
        else:
            print('No')
        T -= 1

if __name__ == "__main__":
    main()