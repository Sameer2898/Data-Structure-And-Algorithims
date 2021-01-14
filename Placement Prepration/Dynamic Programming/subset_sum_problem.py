def isSubsetSum(arr, n, sum): 
    subset = [ [False for j in range(sum + 1)] for i in range(3) ] 
   
    for i in range(n + 1): 
        for j in range(sum + 1): 
            if (j == 0): 
                subset[i % 2][j] = True
            elif (i == 0): 
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j): 
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)  
                                                                               % 2][j] 
            else: 
                subset[i % 2][j] = subset[(i + 1) % 2][j] 
                  
    return subset[n % 2][sum]
  
    
def findPartition(arr,n):
    sm=sum(arr)
    
    if sm%2==0:
        return isSubsetSum(arr, n, sm//2)
    else:
        return
    
if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter the length of the string:- '))
        arr = [int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        if findPartition(arr,n):
            print('YES')
        else:
            print('NO')