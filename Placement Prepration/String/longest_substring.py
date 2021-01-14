def SubsequenceLength(s):
    if len(s) == 0:
        return 0
    
    count = 1
    answer = 1
    
    visited = [-1] * 256
    visited[ord(s[0])] = 0
    for i in range(1, len(s)):
        index = ord(s[i])
        if visited[index] == -1 or i - count > visited[index]:
            count += 1
        else:
            answer = max(count, answer)
            count = i - visited[index]
        visited[index] = i
    return max(count, answer)

for i in range(0,int(input('Enter the number of test cases:- '))):
    s = input('Enter the string:- ')
    print(SubsequenceLength(s))