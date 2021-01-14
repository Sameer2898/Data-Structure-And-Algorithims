def delete_tail(head):
    t = head
    while t.next != head:
        pv = t
        t = t.next
    pv.next = pv.next.next
    return head

def delete_head(head):
    c = head
    while c.next != head:
        c = c.next
    t = head
    head = head.next
    c.next = head
    return head

def get_length(head):
    if not head:
        return 0
    c = 1
    t = head
    while t.next != head:
        t = t.next
        c += 1
    return c

def deleteAtPosition(head,pos):
    if pos == 1:
        return delete_head(head)
    if pos == get_length(head):
        return delete_tail(head)
    curr = head
    pvs = head
    c = 1
    while c < pos:
        c += 1
        pvs = curr
        curr = curr.next
    nxt = curr.next
    curr.next = None
    pvs.next = nxt
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node
    
def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        n = int(input('Enter the size of linked list:- '))
        arr = [int(x) for x in input('Enter the element of the linked list:- ').split()]
        pos=int(input('Enter the position from where elements is to be deleted:- '))
        ll = Llist()
        tail = None
        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        tail.next=ll.head
        resHead=deleteAtPosition(ll.head,pos)
        displayList(resHead)
        print()