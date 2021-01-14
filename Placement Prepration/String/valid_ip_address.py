def isValidIP(s):
    count= 0
    for i in range(0, len(s)):
        if s[i] == '.':
            count += 1
    if count != 3:
        return 0
    st = set()
    for i in range(0, 256):
        st.add(str(i))
    count = 0
    temp = ''
    for i in range(0, len(s)):
        if s[i] != '.':
            temp += s[i]
        else:
            if temp in st:
                count += 1
            temp = ''
    if temp in st:
        count += 1
    if count == 4:
        return 1
    else:
        return 0

if __name__=="__main__":
    t=int(input('Enter the number of test cases:- '))
    for _ in range(0,t):
        s=input('Enter an IP address:- ')
        if(isValidIP(s)):
            print(1)
        else:
            print(0)