def missingPanagram(s):
    arr = {}
    for i in range(0, 26):
        arr[i] = 0
    
    for i in range(0, len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 92):
            arr[ord(s[i]) - ord('A')] = 1
        else:
            arr[ord(s[i]) - ord('a')] = 1
    ans = ''
    for i in range(0, 26):
        if (arr[i] != 1):
            ans += chr(i + ord('a'))
            
    if (ans == ''):
        return '-1'
    return ans

if __name__ == "__main__":
    t = int(input('Enter the number of test cased:- '))
    while(t>0):
        s = input('Enter the character to be found:- ')
        print(missingPanagram(s))
        t = t-1