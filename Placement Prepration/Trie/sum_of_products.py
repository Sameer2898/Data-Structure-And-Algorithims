dp = [[0 for _ in range(1000)] for _ in range(1001)]

def sumOfProduct(arr,n,k):
    # filling last column : n-1 th element
    for r in range(k+1):
        dp[r][n-1]=0
    
    # filling row 1:
    dp[1][n-1]=arr[n-1]
    for c in range(n-2,-1,-1):
        dp[1][c] = ( dp[1][c+1] + arr[c] ) % 1000000007
    
    for c in range(n-2,-1, -1):
        for r in range(2,k+1):
            dp[r][c] = dp[r][c+1] + dp[r-1][c+1] * arr[c]
            dp[r][c] = dp[r][c] % 1000000007
    
    return dp[k][0]

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        line = input('Enter the size of the array and the subarray:- ').strip().split()
        n=int(line[0])
        k = int(line[1])
        arr = [int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        print(sumOfProduct(arr,n,k))