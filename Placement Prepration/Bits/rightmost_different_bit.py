import math

def right_most_bit(n):
    return math.log2(n&-n)+1

def posOfRightMostDiffBit(m,n):
    if m == n:
        return -1
    return right_most_bit(m^n)

def main():
    
    T = int(input('Enter number of test cases:- '))
    while(T>0):
        mn = [int(x) for x in input('Enter a number:- ').strip().split()]
        m = mn[0]
        n = mn[1]
        print(math.floor(posOfRightMostDiffBit(m,n)))        
        T-=1

if __name__=="__main__":
    main()