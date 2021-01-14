def insertion(arr, n, gap):
    ans = 0
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            ans += (abs(arr[i] - arr[i - 1]) - 1) // gap
    return ans

def minimizeMaxDiff(arr,n,k):
    low = 1
    high = 1
    for i in range(1, n):
        high = max(high, abs(arr[i] - arr[i - 1]))
    
    while (high > low):
        mid = (high + low) // 2
        if insertion(arr, n, mid) <= k:
            high = mid
        else:
            low = mid + 1
    return high

if __name__=="__main__":
    t=int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n=int(input('Enter the size of the array:- '))
        arr=[int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        k=int(input())
        print(minimizeMaxDiff(arr,n,k))