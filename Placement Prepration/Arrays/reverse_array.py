def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start + 1, end - 1)

arr = list(map(int, input('Enter the array elements:- ').split(',')))
print(f'The array is:- {arr}')
start = arr[0]
end = len(arr) - 1
reverseArray(arr, start, end)
print('Reversed Array is:-')
for i in range(len(arr)):
    print(arr[i], end=' ')

# bubbleSort(arr)
# print('sorted array:-')
# for i in range(len(arr)):
#     print(arr[i], end=' ')