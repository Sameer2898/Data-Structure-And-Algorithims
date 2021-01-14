def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)

def findingTrailingZeros(n):
    count = 0
    i = 5
    while(n/i>=1):
        count += int(n/i)
        i *= 5
    return int(count)

n = int(input('Entet a number:- '))
print(f'Factorial of {n} is:- {factorial(n)}.')
print(f"Count of zero's in {n}! is:- {findingTrailingZeros(n)}.")