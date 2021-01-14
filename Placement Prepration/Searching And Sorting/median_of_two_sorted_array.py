def maximum(arr1, arr2):
    return arr1 if arr1 > arr2 else arr2
    
def minimum(arr1, arr2):
    return arr1 if arr1 < arr2 else arr2

def findMedianSortedArrays(arr1, n, arr2, n2):
    median = 0
    i = 0
    j = 0
    min_index = 0
    max_index = n
    
    while (min_index <= max_index):
        i = ((min_index + max_index) // 2)
        j = (((n + n2 + 1) // 2) - i)
        
        if (i < n and j > 0 and arr2[j - 1] >= arr1[i]):
            min_index = i + 1
            
        elif (i > 0 and j < n2 and arr2[j] < arr1[i - 1]):
            max_index = i - 1
        
        else:
            if (i == 0):
                median = arr2[j - 1]
            elif ( j == 0):
                median = arr1[i - 1]
            else:
                median = maximum(arr1[i - 1], arr2[j - 1])
            break
        
    if ((n + n2) % 2 == 1):
        return median
    
    if (i == n):
        return ((median + arr2[j]) // 2)
    
    if (j == n2):
        return ((median + arr1[i]) // 2)
    
    return ((median + minimum(arr1[i], arr2[j])) // 2)

if __name__ == '__main__': 
    t=int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        
        n1,n2=list(map(int,(input('Enter the size of the array:- ').split())))
        arr1=list(map(int,(input('Enter element of the first array:- ').split())))
        arr2=list(map(int,(input('Enter element of the second array:- ').split())))
        
        if n1<n2:
            print(findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(findMedianSortedArrays(arr2,n2, arr1,n1))