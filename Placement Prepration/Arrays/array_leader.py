def leaders(A,N):
    ans = []
    max_element = A[N-1]
    for i in range(N-1, -1, -1):
        if A[i] >= max_element:
            max_element = A[i]
            ans.append(max_element)
    ans.reverse()
    return ans

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        N = int(input('Enter how many elements you want to store in array:- '))
        A = [int(i) for i in input('Enter the array elements:- ').strip().split()]
        A = leaders(A, N)
        for i in A:
            print(i, end=' ')
        print()
        T -= 1

if __name__ == "__main__":
    main()