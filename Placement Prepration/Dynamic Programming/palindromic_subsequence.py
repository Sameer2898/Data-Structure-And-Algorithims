def countPs(str):
    n = len(str)
    cps = [[0 for i in range(n + 2)] for j in range(n + 2)]
    for i in range(n):
        cps[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n):
            k = l + i - 1
            if k < n:
                if (str[i] == str[k]):
                    cps[i][k] = (cps[i][k - 1] + cps[i + 1][k] + 1)
                else:
                    cps[i][k] = (cps[i][k - 1] + cps[i + 1][k] - cps[i + 1][k - 1])
    return cps[0][n - 1]

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        print(countPs(input('Enter the string:- ').strip()))