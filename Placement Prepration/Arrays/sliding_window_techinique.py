import sys
int_min = -sys.maxsize - 1

def maxSum(arr, n, k):
    if not n > k: 
        print("Invalid") 
        return -1
    max_sum = int_min
    window_sum = sum(arr[:k]) 
    for i in range(n-k): 
        window_sum = window_sum - arr[i] + arr[i + k] 
        max_sum = max(window_sum, max_sum) 
    return max_sum 

arr = list(map(int, input('Enter the array elements:- ').split(',')))
print(f'Aray elements are:-\n{arr}')
k = int(input('Enter the value of k:- '))
n = len(arr)
print(f'Maximum sum of the array is:\n{maxSum(arr, n, k)}')