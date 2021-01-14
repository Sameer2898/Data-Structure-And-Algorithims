def reverse(head, k):
    current = head
    next = None
    prev = None
    count = 0
    
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    
    if next is not None:
        head.next = reverse(next, k)
    
    return prev

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()
    
if __name__ == '__main__':
    t = int(input('Enter the number oftest cases:- '))
    while (t > 0):
        llist = LinkedList()
        n = input('Enter the size of the linked list:- ')
        values = list(map(int, input('Enter the elements of the linked list:- ').split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input('Enter the size to split the list:- '))
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1