def TopK (arr, n, k):
    um = {}
    for i in range(n):
        if arr[i] in um:
            um[arr[i]] += 1
        else:
            um[arr[i]] = 1
        
    a = [0] * (len(um))
    j = 0
    for i in um:
        a[j] = [i, um[i]]
        j +=  1
    a = sorted(a, key = lambda x:x[0], reverse=True)
    a = sorted(a, key = lambda x:x[1], reverse=True)

    ans = []
    for i in range(k):
        ans.append(a[i][0])
    return ans

t = int (input('Enter the number of test cases:- '))
for tc in range (t):
    inp = list(map(int, input('Enter the size of the array:- ').split()))
    n = inp[0]
    arr = inp[1:]
    k = int (input('Enter the elements of the array:- '))
    res = TopK (arr, n, k)
    for i in res:
        print (i, end = " ")
    print()