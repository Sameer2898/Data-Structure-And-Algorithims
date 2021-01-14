import atexit
import io
import sys

def knapSack(W, wt, val, n):
    k = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or  w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max(val[i - 1] + k[i - 1][w - wt[i - 1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]
    return k[n][W]

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        n = int(input('Enter the size of the knapsack:- '))
        W = int(input('Enter the weight of the items:- '))
        val = list(map(int,input('Enter the value for knapsack:- ').strip().split()))
        wt = list(map(int,input('Enter the value for wieght:- ').strip().split()))
        print(knapSack(W,wt,val,n))