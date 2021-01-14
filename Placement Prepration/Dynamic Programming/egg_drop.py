import atexit
import io
import sys

def eggDrop(n, k):
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    for j in range(1, k + 1):
        eggFloor[1][j] = j
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = float("inf")
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
    return eggFloor[n][k]

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        n,k = map(int,input('Enter the number of eggs and floor:- ').strip().split())
        print(eggDrop(n,k))