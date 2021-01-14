import math

def celsiusToFahrenheit(c):
    return c*9/5+32

def main():
    T = int(input('Enter the number of test cases:- '))
    while T > 0:
        celsius = int(input('Enter the celsius value:- '))
        print(f'The value in farhenheit is:- {math.floor(celsiusToFahrenheit(celsius))}')
        T -= 1

if __name__ == "__main__":
    main()