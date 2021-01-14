def sortedInsert(head, data):
    new_node = Node(data)
    current = head
    
    if current is None:
        new_node.next = new_node
        head = new_node
        return head
    
    elif current.data >= new_node.data:
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return new_node
    
    else:
        while current.next != head and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head
    
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.last=None

    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
if __name__ =='__main__':
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        n = int(input('Enter the size of the linked list:- '))
        arr=[int(x) for x in input('Enter the element of the linked list:- ').split()]
        data=int(input())
        cll=LinkedList()
        for e in arr:
            cll.push(e)
        reshead=sortedInsert(cll.head,data)
        printList(reshead)
        print()