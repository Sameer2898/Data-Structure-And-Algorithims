def maxLen(n, arr):
    hash_map = {}
    max_len = 0 
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if arr[i] is 0 and max_len is 0:
            max_len = 1
        if current_sum is 0:
            max_len = i + 1
        if current_sum in hash_map:
            max_len=n = max(max_len, i - hash_map[current_sum])
        else:
            hash_map[current_sum] = i
    return max_len

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the element of the array:- ').strip().split()))
        print(maxLen(n ,arr))