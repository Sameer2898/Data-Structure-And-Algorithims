def isLucky(n):
    global c
    if c <= n:
        if n % c == 0:
            return 0
        n = n-n//c
        c += 1
        return isLucky(n)
    else:
        return 1
    
c=2
if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        c=2
        n = int(input('Enter a number:- '))
        print(isLucky(n))
        