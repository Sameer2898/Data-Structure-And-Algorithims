a = int(input('Enter the number of an A.P series:- '))
n = int(input('Enter the total number in A.P series:- '))
d = int(input('Enter the common difference:- '))

total = (n*(2*a+(n-1)*d))/2
tn = a+(n-1) * d
i = a
print(f'The sum of A.P. series:- {total}.')
print(f'The term of A.P series:- {tn}')
while i <= tn:
    if i != tn:
        print(i, '+', end=' ')
    else:
        print(i, '=', total)
    i += d