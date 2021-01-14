import atexit
import io
import sys

def sumUnderModulo(a, b):
    M = 1000000007
    return (a % M + b % M) % M

if __name__ == "__main__":
    test_case = int(input('Enter number of test cases:-'))
    for i in range(test_case):
        a, b = map(int, input().strip().split())
    print(f'Sum are:-{sumUnderModulo(a, b)}')