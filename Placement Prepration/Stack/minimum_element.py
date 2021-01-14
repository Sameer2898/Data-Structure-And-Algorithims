class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if not self.s:
            self.minEle = x
            self.s.append(x)
            return
        if x < self.minEle:
            self.s.append(2 * x - self.minEle)
            self.minEle = x
        else:
            self.s.append(x)
            
    def pop(self):
        if not self.s:
            return -1
        top = self.s.pop()
        if top < self.minEle:
            k = self.minEle
            self.minEle = 2 * k - top
            return k
        else:
            return top
        
    def getMin(self):
        if not self.s:
            return -1
        else:
            return self.minEle

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for _ in range(t):
        q = int(input('Enter the size of the stack:- '))
        arr = [int(x) for x in input('Enter the element of the stack:- ').split()]
        stk=stack()  
        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]
            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()