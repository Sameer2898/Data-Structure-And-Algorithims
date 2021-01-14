def maxHist(row ,c):
    answer = list()
    top_val = 0
    max_area = 0
    area = 0
    i = 0
    while i < c:
        if (len(answer) == 0) or (row[answer[-1]] <= row[i]):
            answer.append(i)
            i += 1
        else:
            top_val = row[answer[-1]]
            answer.pop()
            area = top_val * i
            
            if (len(answer)):
                area = top_val * (i - answer[-1] - 1)
            max_area = max(area, max_area)
    
    while(len(answer)):
        top_val = row[answer[-1]]
        answer.pop()
        area = top_val * i
        if (len(answer)):
            area = top_val * (i - answer[-1] - 1)
        max_area = max(area, max_area)
    return max_area
    

def maxRectangle(M, n, m):
    answer = maxHist(M[0], m)
    for i in range(1, n):
        for j in range(m):
            if M[i][j]:
                M[i][j] += M[i - 1][j]
        answer = max(answer, maxHist(M[i], m))
    return answer

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        R, C = input('Enter the size of row and column:- ').split()
        a = list(map(int,input('Enter the elements of the matrix:- ').split()))
        j=0
        A=[]
        R = int(R)
        C = int(C)
        for i in range(0,R):
            A.append(a[j:j+C])
            j=j+C
        # print(A)
        print(maxRectangle(A, R, C)) 