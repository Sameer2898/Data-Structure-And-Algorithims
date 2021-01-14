def search(arr, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    
    if arr[l] <= arr[mid]:
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)
        
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)
    
def Search(arr,n,k):
    return search(arr, 0, n - 1, k)

if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = list(map(int, input('Enter the array elements:- ').split()))
        k = int(input('Enter the element to be searched in array:- '))
        print(Search(arr, n, k))
        