def computeLcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while True:
        if ((greater % x == 0)  and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Enter the first number:- '))
num2 = int(input('Enter the second number:- '))
print(f'The LCM of {num1} and {num2} is:- {computeLcm(num1, num2)}.')