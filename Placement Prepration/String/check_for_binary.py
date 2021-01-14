def isBinary(str):
    length = len(str)
    condition = ['0', '1']
    for i in range(length):
        if str[i] not in condition:
            return False
    return True

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        str = input('Enter the input:- ').strip()
        if isBinary(str):
            print (1)
        else:
            print (0)