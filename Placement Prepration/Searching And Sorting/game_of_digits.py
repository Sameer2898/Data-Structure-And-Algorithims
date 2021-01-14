def smallestK(n):
    if (n == 1):
        return 1
     
    count = [0 for i in range(10)]
    for divisor in range(9, 1, -1):
        while (n % divisor == 0):
            count[divisor] += 1
            n = n // divisor
    
    if n > 1:
        return -1
    
    ans = ''
    for j in range(2, 10):
        for k in range(count[j]):
            ans += str(j)
    return ans

if __name__=="__main__":
    t=int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n=int(input('Enter the element:- '))
        print(smallestK(n))
