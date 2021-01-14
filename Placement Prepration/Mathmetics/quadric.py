import cmath
print('Quadric equation is of type:-')
print('a*x**2+b*x+c')
a = int(input('Enter the value of a:- '))
b = int(input('Enter the value of b:- '))
c = int(input('Enter the value of c:- '))
d = (b**2) - (4*a*c)  

sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print(f'The solution are\n{sol1}\n{sol2}')  