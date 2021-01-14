def repeatedStringMatch(A,B):
    S = A
    ret = 1
    while len(S) < len(B):
        S += A
        ret += 1
        
    if B in S:
        return ret
        
    if B in S+A:
        return ret + 1
    
    return -1

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        A = input('Enter the first string:- ').strip()
        B = input('Enter the second string:- ').strip()
        print(repeatedStringMatch(A,B))