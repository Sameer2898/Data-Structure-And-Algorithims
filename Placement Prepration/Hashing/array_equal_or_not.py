def check(arr1, arr2, n):
    mp = {}
    for i in range(n):
        if arr1[i] in mp.keys():
            mp[arr1[i]] += 1
        else:
            mp[arr1[i]] = 1
        
    for i in range(n):
        if arr2[i] not in mp.keys():
            return False
        else:
            mp[arr2[i]] -= 1

    for i in mp.keys():
        if mp[i] != 0:
            return False
    return True

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for tc in range(t):  
        n = int(input('Enter the size of the array:- '))
        arr1 = [int(x) for x in input('Enter the elements of the first array:- ').replace('  ',' ').strip().split(' ')]
        arr2 = [int(x) for x in input('Enter the elements of the first array:- ').replace('  ',' ').strip().split(' ')]
        if check(arr1, arr2, n):
            print(1)
        else:
            print(0)