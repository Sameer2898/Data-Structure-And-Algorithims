def copyList(head):
    d = dict()
    if not head:
        return
    ch = Node(head.data)
    chh = ch
    d[head] = ch
    h = head.next

    while h:
        nn = Node(h.data)
        chh.next = nn
        d[h] = nn
        h = h.next
        chh = nn
    h = head
    chh = ch
    while h:
        if h.arb:
            chh.arb = d[h.arb]
        h = h.next
        chh = chh.next
    return ch

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    while head and res:
        if id(head)==id(res):
            return
        
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    return True

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for cases in range(t):
        n,m = list(map(int, input('Enter the value two of pointer to split the linked list:- ').strip().split()))
        nodes = list(map(int, input('Enter the nodes:- ').strip().split()))
        aarb = list(map(int, input('Enter the arbitrary pointer:- ').strip().split()))
        ll=LinkedList()
        ll.head=Node(nodes[0])
        tail=ll.head
        
        for x in nodes[1:]:
            tail=insert(tail,x)
        
        for i in range(0,len(aarb),2):
            setarb(ll.head,aarb[i],aarb[i+1])
        
        res=copyList(ll.head)
        if validation(ll.head,res):
            print(1)
        else:
            print(0)