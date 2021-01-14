import math

def isPowerofTwo(n):
    if n == 0:
        return False
    answer = int(math.log2(n))
    return (math.pow(2, answer) == n)

def main():  
    T = int(input('Enter the number of test cases:- '))
    while(T>0):
        n = int(input('Enter a number:- '))
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        T-=1

if __name__=="__main__":
    main()