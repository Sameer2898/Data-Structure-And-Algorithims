def majorityWins(arr, n,  x,y):
    counter_x = 0
    counter_y = 0
    for i in range(0, n):
        if arr[i] == x:
            counter_x += 1
        if arr[i] == y:
            counter_y += 1
    
    if counter_x > counter_y or (counter_x == counter_y and x < y):
        return x
    else:
        return y
    
if __name__ == "__main__":
    T = int(input('Enter number of test cases:- '))
    while T > 0:
        n = int(input('Enter how many elements you want to store in array:- '))
        arr = [int(x) for x in input('Enter array elements- \n').strip().split()]
        x, y = map(int, input('enter the value of x and y:- ').strip().split())
        print('Majority of repetation of element:-')
        print(majorityWins(arr, n, x, y))
        T -= 1