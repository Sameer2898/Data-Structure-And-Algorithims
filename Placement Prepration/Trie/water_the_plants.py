def min_sprinklers(gallery,n):
    s = []
    for i in range(n):
        if gallery[i] > -1:
            s.append([i - gallery[i], i + gallery[i]])
    s.sort()
    target = 0
    s_on = 0
    i = 0
    while(target < n):
        if i == len(s) or s[i][0] > target:
            return -1
        max_range = s[i][1]
        while(i + 1 < len(s) and s[i + 1][0]<= target):
            i += 1
            max_range = max(max_range, s[i][1])
        if max_range < target:
            return -1
        s_on += 1
        target = max_range + 1
        i += 1
    return s_on

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter the size of the array:- '))
        gallery = [int(x) for x in input('Enter the elements of the array:- ').strip().split()]
        print(min_sprinklers(gallery,n))