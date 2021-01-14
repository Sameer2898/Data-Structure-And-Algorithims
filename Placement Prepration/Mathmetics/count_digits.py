import math
def countDigit(n):
    return math.floor(math.log(n, 10) + 1)
num = int(input('Enter a number:- '))
ans = countDigit(num)
print(f'The digit in {num} are:- {ans}.')