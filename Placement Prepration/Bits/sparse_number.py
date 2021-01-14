import math

def isSparse(n):
    return (n & (n >> 1)) == 0

def main():
    T=int(input('Enter the number of test cases:- '))
    while(T>0):
        n=int(input('Enter the input:- '))
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()