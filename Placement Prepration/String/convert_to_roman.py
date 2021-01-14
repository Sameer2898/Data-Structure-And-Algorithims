def convertRoman(n):
    roman = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
             ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
             ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
             ['', 'M', 'MM', 'MMM', '', '', '', '', '', '']]
    i = 0
    str = ''
    while (n != 0):
        str = roman[i][n%10] + str
        n = n //10
        i += 1
    return str

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the number whom you want to convert to roman:- '))
        print(convertRoman(n))