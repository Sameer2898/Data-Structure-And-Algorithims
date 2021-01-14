from collections import deque

def Reduced_String(k,s):
    q = deque()
    for c in s:
        if len(q) and q[-1][0] == c:
            q[-1][1] += 1
            if q[-1][1] == k:
                q.pop()
        else:
            q.append([c,1])
    
    ret = ''
    while len(q):
        ret += q[0][0] * q[0][1]
        q.popleft()
    return ret


if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        k = int(input('Enter the number of element to be split:- '))
        s = input('Enter the string:- ').strip()
        print(Reduced_String(k,s))