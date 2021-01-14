import atexit
import io
import sys

def largestNum(n,s):
    if (9*n<s):
        return -1
    else:
        if n == 1 or s == 0:
            return s
        nines = s // 9
        s %= 9
        ans = '9' * nines
        if len(ans) < n:
            ans += str(s)
            for i in range(n - nines - 1):
                ans += '0'
        return ans
    
if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,s = map(int,input('Enter the lenght and the sum of the password:- ').strip().split())
        print(largestNum(n,s))