def findLongestConseqSubseq(arr, n):
    max1 = 1
    for i in arr:
        j = i
        count = 0
        while(j in arr):
            count+=1
            j+=1
        if(count>max1):
            max1 = count
    return max1 

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = list(map(int, input('Enter the size of the array:- ').strip().split()))
        arr = list(map(int, input('Enter the elements of the array:- ').strip().split()))
        print(findLongestConseqSubseq(arr, n[0]))