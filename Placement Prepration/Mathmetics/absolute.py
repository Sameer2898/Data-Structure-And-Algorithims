def absolute(I):
    return abs(I)

def main():
    T = int(input('Enter how many times you wnat to check the value:- '))
    while T > 0:
        num = int(input('Enter the value:- '))
        print(f'Absolute value is:- {absolute(num)}')
        T -= 1

if __name__ == "__main__":
    main()