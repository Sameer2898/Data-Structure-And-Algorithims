def toString(List):
    return  ''.join(List)

def permute(a, l, r, answer):
    if l == r:
        answer.append(toString(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i],  a[l]
            permute(a, l+1, r, answer)
            a[l], a[i] = a[i], a[l]

def permutation(S):
    a = list(S)
    n = len(S)
    answer = []
    permute(a, 0, n-1, answer)
    answer.sort()
    for i in answer:
        print(i, end=' ')

def main():
    T = int(input('Enter number of test cases:- '))
    while(T>0):
        S = input('Enter a string:- ')
        permutation(S)
        print()
        T-=1

if __name__=="__main__":
    main()