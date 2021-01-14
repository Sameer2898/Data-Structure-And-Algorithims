class lst_entry:
    def __init__(self, x, y, z):
        self.val = x
        self.lst = y
        self.inx = z

class min_heap:
    def __init__(self):
        self.heap_lst = []

    def add(self, x, y, z):
        self.heap_lst.append(lst_entry(x, y, z))
        index = len(self.heap_lst) - 1
        while(index > 0 and self.heap_lst[index].val < self.heap_lst[(index - 1) // 2].val):
            parent = (index - 1) // 2
            self.heap_lst[index], self.heap_lst[parent] = self.heap_lst[parent], self.heap_lst[index]
            index = parent
    
    def pop(self):
        ret = (self.heap_lst[0].val, self.heap_lst[0].lst, self.heap_lst[0].inx)
        l = len(self.heap_lst)
        self.heap_lst[0] = self.heap_lst[l - 1]
        self.heap_lst.pop()
        l = l -1
        i = 0
        while (1):
            if (2 * i + 1 >= l):
                break
            child = 2 * i + 1
            if (2 * i + 2 < l and self.heap_lst[2 * i +2].val < self.heap_lst[2 * i + 1].val):
                child = 2 * i + 2
            if (self.heap_lst[child].val >= self.heap_lst[i].val):
                break
            self.heap_lst[i] , self.heap_lst[child] = self.heap_lst[child], self.heap_lst[i]
            i = child
        return ret
    
    def available(self):
        if (len(self.heap_lst) > 0):
            return True
        return False
        
def merge(numbers):
    n = len(numbers)
    h = min_heap()
    for i in range(n):
        h.add(numbers[i][0], i, 0)
    arr = []
    while (h.available()):
        val, i, j = h.pop()
        arr.append(val)
        if (j + 1 < len(numbers[i])):
            h.add(numbers[i][j + 1], i, j + 1)
    return arr

if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        n = int(input('Enter the size of the heap:- '))
        numbers = [[ 0 for _ in range(n) ] for _ in range(n) ]
        line = input('Enter the elements of the heap:- ').strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i*n+j])
        merged_list = merge(numbers)
        for i in merged_list:
            print(i,end=' ')
        print()