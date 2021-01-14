def multiply(a,b):
    integer_a = int(a)
    integer_b = int(b)
    return (integer_a * integer_b)

if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        a,b = input('Enter the two numebrs to multiply:- ').split()
        print(multiply( a.strip() , b.strip() ))