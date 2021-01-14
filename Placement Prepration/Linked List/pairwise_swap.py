class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

def pairWiseSwap(head):
    a = head
    b, c, prev = None, None, None
    while a and a.next:
        b = a.next
        c = b.next
        if a == head:
            head = b
        else:
            prev.next = b
        b.next = a
        a.next = c
        prev = a
        a = c
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for i in range(int(input('Enter the number of test cases:- '))):
        n = int(input('Enter the size of the linked list:- '))
        arr = [int(x) for x in input('Enter the elements of the linked list:- ').split()]
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        head = pairWiseSwap(lis.head)
        printList(head)