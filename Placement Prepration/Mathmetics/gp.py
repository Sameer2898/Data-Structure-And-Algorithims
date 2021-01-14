def printGp(a, r, n):
    for i in range(0, n):
        curr_term = a * pow(r, i)
        print(curr_term, end=' ')
a = int(input('Enter the number of an A.P series:- '))
r = int(input('Enter the total number in A.P series:- '))
n = int(input('Enter the common difference:- '))
printGp(a, r, n)