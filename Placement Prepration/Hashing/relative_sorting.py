def relativeSort (A1, N, A2, M):
    d = {}
    for i in A1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    ans = []
    an = []
    arr = set(A1) - set(A2)
    for i in arr:
        if i in d:
            an.extend([i] * d[i])
    for i in A2:
        if i in d:
            ans.extend([i] * d[i])
    l1 = list(an)
    l1.sort()
    ans.extend(l1)
    return ans

t = int (input('Enter the number of test cases:- '))
while t > 0:
    n, m = list(map(int, input('Enter the size of two arrays:- ').split()))
    a1 = list(map(int, input('Enter the element of the first array:- ').split()))
    a2 = list(map(int, input('Enter the element of the second array:- ').split()))
    a1 = relativeSort (a1, n, a2, m)
    for i in a1:
        print (i, end = " ")
    print ()
    t -= 1