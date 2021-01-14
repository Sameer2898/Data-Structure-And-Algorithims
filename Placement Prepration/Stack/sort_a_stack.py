def sorted(s):
    return s.sort(reverse = True)

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the stack:- '))
        arr = list(map(int, input('Enter the element of the stack:- ').strip().split()))
        sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(0), end=" ")
        print()