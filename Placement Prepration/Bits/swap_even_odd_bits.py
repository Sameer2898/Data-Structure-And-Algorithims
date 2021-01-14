import math

def swapBits(n):
    even = n&0xAAAAAAA
    odd = n&0x5555555
    even >>= 1
    odd <<= 1
    return even|odd

def main(): 
    T = int(input('Enter number of test cases:- '))   
    while(T>0):
        n = int(input('Enter a number:- '))
        print(swapBits(n))
        T-=1

if __name__=="__main__":
    main()