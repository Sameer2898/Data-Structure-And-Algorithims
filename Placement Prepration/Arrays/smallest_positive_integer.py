def segregate(arr, size):
    j = 0
    for i in range(size):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j
    
def findMissingPostitve(arr, size):
    for i in range(size):
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    for i in range(size):
        if arr[i] > 0:
            return i + 1
    return size + 1


def findMissing(arr, size): 
    shift = segregate(arr, size)
    return findMissingPostitve(arr[shift:], size - shift)

if __name__ == "__main__":
    t = int(input('Enter the number of the test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the array element:- ').strip().split()))
        print(f'Missing smallest element is:- {findMissing(arr, n)}')