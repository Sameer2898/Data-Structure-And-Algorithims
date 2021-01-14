def binarySearch(arr, left, right, k):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binarySearch(arr, left, mid - 1, k)
    else:
        return binarySearch(arr, mid + 1, right, k)
    
print('Enter array element:-')
arr = list(map(int, input().split()))
print(f'The array is:- {arr}')
x = int(input('Enter element to search:- '))
ans = binarySearch(arr, 0, len(arr)-1, x)
if ans != -1:
    print(f'{x} is present in {arr}.')
else:
    print(f'{x} is not present in {arr}.')