def getMaxArea(histogram):
    stack = []
    max_area = 0
    index = 0
    while index < len(histogram):
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (histogram[top] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        area = (histogram[top] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    return max_area

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n = int(input('Enter the size of the array:- '))
        a = list(map(int,input('Enter the elements of the array:- ').strip().split()))
        print(getMaxArea(a))