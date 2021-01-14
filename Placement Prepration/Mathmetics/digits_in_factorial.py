import math 

def digitsInFactorial(N):
    if N < 0:
        return 0
    if N <= 1:
        return 1
    digits = 0
    for i in range(2, N+1):
        digits += math.log10(i)
    return math.floor(digits) + 1

def main():
    T = int(input('Enter number of test cases:- '))
    while T > 0:
        num = int(input('Enter the number:- '))
        print(f'Digits in factorial of num is:- {digitsInFactorial(num)}')
        T -= 1

if __name__ == "__main__":
    main()


    