def printNonRepeated(arr,n):
    dict = {}
    for i in arr:
        dict[i] = 0
    
    for i in arr:
        dict[i] += 1
    
    l = []
    for i in arr:
        if dict[i] == 1:
            l.append(i)
    return l

def main():
    T = int(input('Enter the number of test cases:- '))
    while(T>0):
        n = int(input('Enter the size of the array:- '))
        arr = [int(x) for x in input('Enter the element of the array:- ').strip().split()]
        l = printNonRepeated(arr,n)
        print(*l)
        T-=1

if __name__=="__main__":
    main()