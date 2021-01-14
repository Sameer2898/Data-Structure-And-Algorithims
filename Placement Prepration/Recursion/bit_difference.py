def sumBitDiff(arr,n): 
    answer = 0
    for i in range(0, 32):
        count = 0
        for j in range(0, n):
            if arr[j] & (1 << i):
                count += 1
        answer += (count * (n - count) * 2)
    return answer

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the array:- '))
        arr=[int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        print(sumBitDiff(arr,n))