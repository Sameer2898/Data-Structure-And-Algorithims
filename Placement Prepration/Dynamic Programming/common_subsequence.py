import atexit
import io
import sys

def lcs(m,n,X,Y):
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        m,n = map(int,input('Enter the length of two strings:- ').strip().split())
        X = str(input('Enter the first string:- '))
        Y = str(input('Enter the second string:- '))
        print(lcs(m,n,X,Y))