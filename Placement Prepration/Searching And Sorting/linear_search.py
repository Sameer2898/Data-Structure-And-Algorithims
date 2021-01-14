def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

print('Enter array element:-')
arr = list(map(int, input().split()))
print(f'The array is:- {arr}')
x = int(input('Enter element to search:- '))
n = len(arr)
ans = linearSearch(arr, n, x)
if ans == -1:
    print(f'{x} is not present in {arr}.')
else:
    print(f'{x} is present in {arr}.')