def remove_duplicate(n, arr):
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    j = 0
    for i in range(0, n-1):
        if arr[i] != arr[i +1]:
            temp[j] = arr[i]
            j += 1
    temp[j] = arr[n - 1]
    j += 1
    for i in range(0, j):
        arr[i] = temp[i]
    return j

if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('How namy elements you want to insert to array:- '))
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print(f'Array after removing duplicate elements:- {arr[i]}')
            # print(arr[i], end=' ')
        print()    