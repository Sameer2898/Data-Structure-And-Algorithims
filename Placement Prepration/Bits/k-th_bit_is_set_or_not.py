import math

def checkKthBit(n,k):
    return ((n&(1<<(k)))!=0)

def main():
    T=int(input('Enter the number of test cases:- '))  
    while(T>0):
        n=int(input('Enter the number:- '))
        k=int(input('Enter the number whose bit you want to find:- '))
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")   
        T-=1

if __name__=="__main__":
    main()