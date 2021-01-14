import math

def getFirstSetBit(n):
    if n == 0:
        return 0
    return math.ceil(math.log2(n&-n)+1)

def main():  
    T = int(input('Enter the number of test cases- '))
    
    while(T>0):
        n = int(input('Enter a number:- '))
        print(getFirstSetBit(n))
        T-=1

if __name__=="__main__":
    main()