def remainderWith7(str):
    return int(str) % 7

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        str = input('Enter the number:- ').strip()
        print(remainderWith7(str))