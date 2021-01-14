def intersction(a, b, n, m):
    i = 0
    j = 0
    flag = False
    l = []
    while i < n and  j < m:
        if i > 0 and a[i-1] == a[i]:
            i += 1
            continue
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            l.append(b[j])
            flag = True
            i += 1
            j += 1
    if flag is False:
        l.append(b[j])
    return l

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,m = map(int,input('Enter the size of the array').strip().split())
        a = list(map(int,input(f'Enter the {n} array element:- ').strip().split()))
        b = list(map(int,input(f'Enter the {m} array element:- ').strip().split()))
        l = intersction(a,b,n,m)
        print(*l)