def josephus(n,k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1

def main():  
    T = int(input('Enter the number of test cases:- '))
    while(T>0):
        nk=[int(x) for x in input('Enter a number:- ').strip().split()]
        n=nk[0]
        k=nk[1]
        print(josephus(n,k))
        T-=1

if __name__=="__main__":
    main()