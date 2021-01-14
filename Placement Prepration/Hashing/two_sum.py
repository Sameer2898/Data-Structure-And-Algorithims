def keypair(A, N, X):
    s = dict()
    for i in range(0, n):
        temp = x - a[i]
        if s.get(temp):
            return True
        s[a[i]] = 1
    return False

t = int(input('Enter the number of test cases:- '))
for _ in range(0,t):
    n,x=list(map(int,input('Enter the size of the array and number to find in array:- ').split()))
    a=list(map(int,input('Enter elements of the array:- ').split()))
    sln=keypair(a,n,x)
    if(sln):
        print("Yes")
    else:
        print("No")