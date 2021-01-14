def Push(x,stack1,stack2):
    stack1.append(x)

def Pop(stack1,stack2):
    if not stack2:
        if not stack1:
            return -1
        
        while stack1:
            r = stack1.pop()
            stack2.append(r)
        k = stack2.pop()
        
        while stack2:
            l = stack2.pop()
            stack1.append(l)
        return k
    return -1

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        qry = int(input('Enter the size of the queue:- '))
        qtyp_qry=list(map(int, input('Enter the elements of the queue:- ').strip().split()))
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1     
        print()