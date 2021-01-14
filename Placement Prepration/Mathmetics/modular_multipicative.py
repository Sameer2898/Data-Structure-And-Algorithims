def modInverse(a,m):
    a = a%m
    for i in range(1, m):
        if ((a*i)%m == 1):
            return i
    return -1

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        am = [int(i) for i in input().strip().split()]
        a = am[0]
        m = am[1]
        print(f'The mod inverse is:- {modInverse(a, m)}')
        T -= 1

if __name__ == "__main__":
    main()