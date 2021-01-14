def findSubArrays(arr,n):
    c = 0
    hashmap = {}
    out = []
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
        if sum1 == 0:
            out.append((0, i))
            c += 1
        al = []
        
        if sum1  in hashmap:
            al = hashmap.get(sum1)
            for j in range(len(al)):
                out.append((al[j] + 1, i))
                c += 1
        al.append(i)
        hashmap[sum1] = al
    return c

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for tc in range(t):
        N = int(input('Enter the size of the array:- '))
        A = [int(x) for x in input('Enter the elements of the array:- ').strip().split(' ')]
        print(findSubArrays(A,N))