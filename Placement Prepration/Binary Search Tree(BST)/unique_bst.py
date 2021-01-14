def numTrees(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1,  i + 1):
            dp[i] = dp[i] + (dp[i - j] * dp[j - 1])
            if dp[i] >= 1000000007:
                dp[i] = dp[i] % 1000000007
    return dp[n]

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(0,t):
        n = int(input('Enter the elements of the tree:- '))
        print(numTrees(n))