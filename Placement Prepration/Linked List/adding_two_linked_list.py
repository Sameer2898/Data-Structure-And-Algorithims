class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    next = None
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
    
def addLists(first, second):
    first = reverse(first)
    second = reverse(second)
    sum_list = None
    carry = 0
    
    while first is not None or second is not None or carry > 0:
        new_val = carry
        if first is not None:
            new_val += first.data
        if second is not None:
             new_val += second.data
        
        carry = new_val//10
        new_val = new_val%10
        new_node = Node(new_val)
        new_node.next = sum_list
        sum_list = new_node
        
        if first:
            first = first.next
        if second:
            second = second.next
    return sum_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input('Enter the number of test cases:- '))):
        
        n = int(input('Enter the size of the first linked list:- '))
        arr1 = ( int(x) for x in input('Enter the element of first linked list:- ').split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input('Enter the size of the second linked list:- '))
        arr2 = ( int(x) for x in input('Enter the element of second linked list:- ').split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addLists(LL1.head, LL2.head)
        printList(res)