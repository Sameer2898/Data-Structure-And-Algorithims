import math

def grayToBinary(n):
    ans = 0
    while n > 0:
        ans = (ans^n)
        n = (n >> 1)
    return ans

def main():  
    T = int(input('Enter the number of test cases:- '))
    while(T>0):
        n = int(input('Enter a number:- '))
        print(grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()