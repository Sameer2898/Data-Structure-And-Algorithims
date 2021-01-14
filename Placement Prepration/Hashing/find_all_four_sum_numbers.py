def fourSum(arr, k):
    n = len(arr)
    ans = []
    if (n < 4):
        return ans
    arr.sort()
    for i in range(0, n-3):
        if (arr[i] > 0 and arr[i] > k):
            break
        if (i > 0 and arr[i] == arr[i - 1]):
            continue
        for j in range(i + 1, n - 2):
            if (j > i + 1 and arr[j] == arr[j - 1]):
                continue
            left = j + 1
            right = n - 1
            while (left < right):
                old_l = left
                old_r = right
                sum = arr[i] + arr[j] + arr[left] + arr[right]
                if (sum == k):
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    while (left < right and arr[left] == arr[old_l]):
                        left += 1
                    while (left < right and arr[right] == arr[old_r]):
                        right -= 1
                elif (sum > k):
                    right -= 1
                else:
                    left += 1
    return ans

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    while t:
        t -= 1
        n, k = list(map(int,input('Enter the size of the array:- ').split()))
        # print(n, k)
        a = list(map(int, input('Enter the elemente of the array:-').split()))
        # print(a)
        ans = fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans) == 0):
            print(-1, end="")
        print()
         