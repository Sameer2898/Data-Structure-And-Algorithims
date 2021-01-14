def maxDistance(arr, n):
    max_ele = 0
    for i in arr:
        a = arr.index(i)
        b = len(arr) - arr[::-1].index(i) - 1
        c = b - a
        if c > max_ele:
            max_ele = c
    return max_ele

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the elements of the array:- ').strip().split()))
        print(maxDistance(arr, n))