def modInverse(a,m):
    g = gcd(a, m)
    if(g != 1):
        print('Inverse does not exist.')
    else:
        print(f'Modular multipicative inverse is:- {power(a, m-2, m)}.')

def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    if y % 2 == 0:
        return p
    else:
        return ((x * p) % m)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

a = int(input('Enter a number:- '))
m = int(input('Enter a number of modulo:- '))
modInverse(a, m)