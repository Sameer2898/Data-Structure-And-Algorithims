import math

def greyConverter(n):
    answer = (n >> 1)
    return n^answer

def main():
    T=int(input('Enter the number of test cases:- '))
    while(T>0):
        n=int(input('Enter the number:- '))
        print(greyConverter(n))
        T-=1

if __name__=="__main__":
    main()