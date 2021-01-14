def longestPalindrome(S):
    max_length = 1
    start = 0
    length = len(S)
    low = 0
    high = 0
    for i in range(1, length):
        low = i - 1
        high = i
        while (low >= 0 and high < length and S[low] == S[high]):
            if (high - low + 1 > max_length):
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
            
        low = i - 1
        high = i + 1
        while (low >= 0 and high < length and S[low] == S[high]):
            if (high - low + 1 > max_length):
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    return S[start:start + max_length]

if __name__=='__main__':
    tc = int(input('Enter the number of test cases:- '))
    for i in range(tc):
        str = input('Enter the string')
        print(longestPalindrome(str))