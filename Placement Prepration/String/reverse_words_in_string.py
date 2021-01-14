def reverseWords(s):
    answer = ''
    words = []
    curr_word = ''
    for i in range(len(s)):
        if s[i] == '.':
            words.append(curr_word)
            curr_word = ''
        else:
            curr_word += s[i]
    words.append(curr_word)
    
    for i in range(len(words) - 1,  -1, -1):
        answer += words[i]
        if i:
            answer += '.'
    return answer

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        s = input('Enter the string:- ')
        print(reverseWords(s))