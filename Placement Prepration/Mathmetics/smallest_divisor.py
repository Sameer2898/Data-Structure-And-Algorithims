import math

def getSmallestDivNum(n):
    ans = 1
    for i in range(1, n+1):
        ans = int((ans * i)/math.gcd(ans, i))
    return ans

if __name__ == "__main__":
    t = int(input('Enter how many times you want to execute:- '))
    for tcs in range(t):
        n = int(input(f'Enter {tcs+1} number:- '))
        print(f'Smallest Divisior is:- {getSmallestDivNum(n)}')
    