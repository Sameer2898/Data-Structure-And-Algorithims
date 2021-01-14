def search(matrix, n, m, x): 
    i, j = n - 1, 0
    while(i >= 0 and j < m):
        if matrix[i][j] == x:
            return True
        if matrix[i][j] > x:
            i -= 1
        else:
            j += 1
    return False

if __name__ == '__main__':
	t = int(input('Entet the number of test cases:- '))
	for _ in range(t):
		size = input('Enter the size of the matrix:- ').strip().split()
		r = int(size[0])
		c = int(size[1])
		line = input('Enter the elements:- ').strip().split()
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				matrix[i][j] = int( line[i*c+j] )
		target = int(input())

		if (search(matrix,r,c,target)): 
			print(1) 
		else: 
			print(0) 