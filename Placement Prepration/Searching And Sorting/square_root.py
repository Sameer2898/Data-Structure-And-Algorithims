import math

def floorSqrt(x): 
    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    count = 0
    while start <= end:
        mid = (start + end) //2
        if mid*mid == x:
            return mid
        if mid*mid < x:
            start = mid + 1
            count = mid
        else: 
            end = mid - 1
    return count
    
def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        x = int(input('Enter a number:- '))
        print(floorSqrt(x))
    T -= 1

if __name__ == "__main__":
    main()