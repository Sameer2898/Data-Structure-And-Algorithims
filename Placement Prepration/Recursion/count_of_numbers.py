def printNos(N):
    if (N > 0):
        printNos(N-1)
        print(N, end=' ')
    
def main():
    T = int(input('Enter the number of test cases:- '))
    while(T>0):  
        N = int(input('Enter a  number:- '))
        printNos(N)
        print()
        T -= 1

if __name__=="__main__":
    main()