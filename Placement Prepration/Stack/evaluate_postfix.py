
def reverse(string):
    stack = []
    for ch in string:
        stack.append(ch)
    
    reverse = ''
    while len(stack):
        reverse += stack.pop()
    return reverse

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        str1 = input('Enter the expression:- ')
        print(reverse(str1))