def ExcelColumn(n):
    s = ''
    i = 0
    while n > 0:
        rem = n % 26
        if rem == 0:
            s += 'Z'
            i += 1
            n = (n // 26) - 1
        else:
            s += chr((rem - 1) + ord('A'))
            i += 1
            n = n // 26
    return s[::-1]

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the number to see its equivalent column alphabet:- '))
        print(ExcelColumn(n))