from collections import defaultdict

def countDistinct(arr, N, K):
    mp = defaultdict(lambda:0)
    dist_count = 0
    for i in range(k):
        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1
    ans = []
    ans.append(dist_count)
    for i in range(k, n):
        if mp[arr[i - k]] == 1:
            dist_count -= 1
        mp[arr[i - k]] -= 1
        
        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1
        
        ans.append(dist_count)
    return ans

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n,k = list(map(int, input('Enter the value of n and k:- ').strip().split()))
        arr = list(map(int, input('Enter the elements of the array:- ').strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()