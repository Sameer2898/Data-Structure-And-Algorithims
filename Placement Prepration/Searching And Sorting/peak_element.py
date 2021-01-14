def peakElement(arr, n):
    if n is 1:
        return 0
    for i in range(n):
        if i == 0 and arr[i] < arr[0]:
            return 0
        elif i == n - 1 and arr[n - 2] < arr[n - 1]:
            return n - 1
        elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            return i

if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the array elements:- ').split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n == 1:
            flag = True
        elif index == 0 and arr[index] >= arr[index + 1]:
            flag = True
        elif index == n - 1 and arr[index] >= arr[index - 1]:
            flag = True
        elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
            flag = True
        else:
            flag = False
        
        if flag:
            print(1)
        else:
            print(0)