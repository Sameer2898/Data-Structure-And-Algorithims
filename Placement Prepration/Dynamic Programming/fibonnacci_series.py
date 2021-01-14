def printFibb(n):
    ans = []
    a = b = 1
    if n >= 1:
        ans.append(1)
    if n >= 2:
        ans.append(1)
    for i in range(2, n):
        ans.append(a + b)
        c = a + b
        a = b
        b = c
    return ans

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):    
        n = int(input('Enter the number to find fibonnacci series:- '))
        res = printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()