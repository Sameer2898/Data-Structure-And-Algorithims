from bisect import bisect_left as lower_bound
def findNumOfPair(array, n): 
    array = sorted(array)
    ans = 0
    for i in range(n):
        if (array[i] <= 0):
            continue
        j = lower_bound(array, -array[i] + 1)
        ans += i - j
    return ans

if __name__ == '__main__': 
	t = int(input('Enter the number of test cases:- '))
	for _ in range(t):
		n = int(input('Enter the size of the array:-'))
		array = list(map(int, input('Enter the elements of the array:- ').strip().split()))
		ans = findNumOfPair(array, n) 
		print(ans) 