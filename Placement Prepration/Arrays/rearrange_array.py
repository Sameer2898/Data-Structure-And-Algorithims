def arrange(arr, n): 
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] = arr[i] // n

def main():
    T = int(input('Enter number of test cases:- '))
    while(T > 0):
        n = int(input('Enter the size of the array:- '))
        arr = [int(x) for x in input('Eater the elements of the array:- ').strip().split()]
        arrange(arr, n)
        print('Rotated array is:- ')
        for i in arr:
            print(i, end=' ')
        print()
        T -= 1

if __name__ == "__main__":
    main()