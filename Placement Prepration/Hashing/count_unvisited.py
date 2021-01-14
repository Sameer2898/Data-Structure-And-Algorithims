def countUnvisited(n, m): 
    i = 0
    x = (m * n) - m - n
    queue = []
    queue.append(x)
    set = {x}
    count = 0
    while (len(queue) > 0):
        curr = queue[0]
        queue.remove(queue[0])
        count += 1
        key = curr - m
        if (key > 0 and key not in set):
            queue.append(key)
            set.add(key)
        
        key = curr - n
        if (key > 0 and key not in set):
            queue.append(key)
            set.add(key)
    return count

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
    	arr = list(map(int, input('Enter the value of n and m:- ').strip().split()))
    	n = arr[0]
    	m = arr[1]
    	print(countUnvisited(n, m)) 