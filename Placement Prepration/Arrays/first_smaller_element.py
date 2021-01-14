def immediateSmaller(arr,n,x):
    ans = -1
    diff = 10000000
    for i in arr:
        if i < x and x - i < diff:
            ans = i
            diff = x - i
    return ans

if __name__ == "__main__":
    T = int(input('Enter the number of test cases:- '))
    for i in range(T):
        n = int(input('Enter the size of the array:- '))
        arr = [int(j) for j in input('Enter the element of the array:- ').strip().split()]
        x = int(input('Enter the element whose nearest element to be find:- '))
        ans = immediateSmaller(arr, n, x)
        print(f'The smaller element is:- {ans}.')