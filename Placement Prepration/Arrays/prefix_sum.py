def fillPrefixSum(arr, n, prefixsum):
    prefixsum[0] = arr[0]
    for i in range(1, n):
        prefixsum[i] = prefixsum[i - 1] + arr[i]

arr = list(map(int, input('Enter the array elements:- ').split(',')))
print(f'Aray elements are:-\n{arr}')
n = len(arr)
prefixsum = [0 for i in range(n + 1)]
fillPrefixSum(arr, n, prefixsum)
print('Prefix sum is:-')
for i in range(n):
    print(prefixsum[i], " ", end ="") 