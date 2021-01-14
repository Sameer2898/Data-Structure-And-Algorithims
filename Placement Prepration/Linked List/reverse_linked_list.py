def reverseList(head):
    if head is None:
        return None
    previous = None
    current = head
    next = head.next
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
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

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input('Enter the number of test cases:- '))):
        n = int(input('Enter the size of the likned list:- '))
        arr = [int(x) for x in input('Enter the elements:- ').split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = reverseList(lis.head)
        printList(newHead)