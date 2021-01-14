def MaxSum(arr,n):
    if n == 1:
        return arr[0]
    x = 0
    y = 0
    z = arr[0]
    for i in range(1, n):
        value = max(x + arr[i - 1] + arr[i], y + arr[i], z)
        x, y, z = y, z, value
    return z

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = [int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        print(MaxSum(arr,n))