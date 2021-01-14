def maxSubArraySum(a,size):
    max_so_far = -9999999 - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def main():
    t = int(input('Enter the number of test cases:- '))
    while(t > 0):
        n = int(input('Enter the number of elements:- '))
        arr = [int(j) for j in input('Enter the element of the array:- ').strip().split()]
        print(f'Maximum array sum is:- {maxSubArraySum(arr, n)}')
        t -= 1

if __name__ == "__main__":
    main()