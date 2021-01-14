import math

def countBits(n):
    count = 0
    while(n > 0):
        count += n&1
        n >>= 1
    return count

def countBitsFlip(a,b):
    answer = 0
    answer = a^b
    return countBits(answer)

def main():
    T = int(input('Enter the number of test cases:- '))
    while(T>0):
        ab = [int(x) for x in input('Enter the number:- ').strip().split()]
        a = ab[0]
        b = ab[1]
        print(countBitsFlip(a,b))
        T -= 1

if __name__=="__main__":
    main()