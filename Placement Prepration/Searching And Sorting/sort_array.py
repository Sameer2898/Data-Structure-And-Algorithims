def sort012(arr,n):
    return arr.sort()

if __name__ == '__main__':
    t=int(input('Enter number of test cases:- '))
    for _ in range(t):
        n=int(input('Enter the size of the array:- '))
        arr=[int(x) for x in input('Enter the array eement:- ').strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()