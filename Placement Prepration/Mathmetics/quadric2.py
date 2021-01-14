import math

def quadraticRoots(a,b,c):
    #Your code here
    root1 = 0
    root2 = 0
    temp = pow(b, 2)-4*a*c
    if temp < 0:
        print('Imaginary')
    else:
        root1 = math.floor((-1*b+math.sqrt(temp))/(2*a))
        root2 = math.floor((-1*b-math.sqrt(temp))/(2*a))
        print(max(root1, root2), min(root1, root2))

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        abc = [int(i) for i in input().strip().split()]
        a = abc[0]
        b = abc[1]
        c = abc[2]
        # print(f'Quadric roots are:- {quadraticRoots(a, b, c)}')
        quadraticRoots(a, b, c)
        T -= 1

if __name__ == "__main__":
    main()