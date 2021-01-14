def detectLoop(head):
    hare = head
    turtle = head
    while hare and turtle and turtle.next:
        hare = hare.next
        turtle = turtle.next.next
        if hare == turtle:
            return True
    return False

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
    
    def loopHere(self,pos):
        if pos==0:
            return
        walk = self.head
        for i in range(1,pos):
            walk = walk.next   
        self.tail.next = walk
    
if __name__ == '__main__':
    for i in range(int(input('Enter the number of test cases:- '))):
        n = int(input('Enter the size of the linked list:- '))
        LL = LinkedList()
        for i in input('Enter the element of the linked list:- ').split():
            LL.insert(int(i))
        LL.loopHere(int(input()))
        print(detectLoop(LL.head))