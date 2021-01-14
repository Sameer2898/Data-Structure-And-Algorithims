def binarySearch(lst, l, h, value):
    if value > lst[h]:
        return h+1
    while h>l:
        middle = (h+l)//2
        if lst[middle] == value:
            return middle
        if lst[middle] > value:
            h = middle
        else:
            l = middle + 1
    return h

def longestSubsequence(a,n):
    tail = [0 for _ in range(n)]
    tail[0] = a[0]
    lastIndex = 0 
    for i in range(1,n):
        index = binarySearch( tail, 0, lastIndex, a[i] )
        tail[index] = a[i]
        lastIndex = max( lastIndex, index )
    
    return lastIndex+1

if __name__ == '__main__':
    for _ in range(int(input('Enter the number of test cases:- '))):
        n = int(input('Enter the value:- '))
        a = [ int(x) for x in input().split() ]
        print(longestSubsequence(a,n))