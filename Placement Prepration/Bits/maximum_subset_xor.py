def maxSubarrayXOR(set,n):
    m = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            for k in range(j, n):
                sum = sum^set[k]
                m = max(m, sum)
    return m

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter a number:- '))
        set = list(map(int,input().split()))
        print(maxSubarrayXOR(set,n))