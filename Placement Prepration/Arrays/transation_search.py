def transitionPoint(arr, n):
    if arr[0] == 1:
        return 0

    lb = 0
    ub = n - 1
    while(lb <= ub):
        mid = (int)((lb + ub) / 2)
        if arr[mid] == 0:
            lb = mid + 1
        elif arr[mid] == 1:
            if arr[mid - 1] == 0:
                return mid
            ub = mid - 1
    return -1 

if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the number of elements:- '))
        arr = list(map(int, input('Enter the array elements:- ').strip().split()))
        print(f'Transation point is:- {transitionPoint(arr, n)}')