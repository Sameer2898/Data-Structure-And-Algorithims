def mergeArrays(a,b,n,m):
    union_list = list()
    i, j = 0, 0
    while i < n and j < m:
        while i + 1 < n and a[i+1] == a[i]:
            i += 1
        while j + 1 < m and b[j+1] == b[j]:
            j += 1
        if a[i] < b[j]:
            union_list.append(a[i])
            i += 1
        elif b[j] < a[i]:
            union_list.append(b[j])
            j += 1
        else:
            union_list.append(b[j])
            j += 1
            i += 1
    
    while i < n:
        while i + 1 < n and a[i+1] == a[i]:
            i += 1
        union_list.append(a[i])
        i += 1
        
    while j < m:
        while j + 1 < m and b[j+1] == b[j]:
            j += 1
        union_list.append(b[j])
        j += 1
    return union_list

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,m = map(int,input('Enter the size of the array:- ').strip().split())
        a = list(map(int,input(f'Enter the {n} array element:- ').strip().split()))
        b = list(map(int,input(f'Enter the {m} array element:- ').strip().split()))
        li = mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()