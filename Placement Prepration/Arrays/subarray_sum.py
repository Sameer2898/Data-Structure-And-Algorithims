def subArraySum(arr, n, sum): 
    #Your code here
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i -1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print('%d %d'%(start+1, i), end=' ')
            return -1
        if i < n:
            curr_sum += arr[i]
        i += 1
    print('-1', end=' ')

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        NS = input('Enter the size of array and the sum:- ').strip().split()
        N = int(NS[0])
        S = int(NS[1])
        A = list(map(int, input('Enter the array elements:- ').strip().split()))
        subArraySum(A, N, S)
        print()
        T -= 1

if __name__ == "__main__":
    main()