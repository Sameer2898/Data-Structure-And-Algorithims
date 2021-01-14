def deleteMid(head):
    if head is None or head.next is None:
        return None
    prev, slow, fast = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = slow.next
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


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        n = int(input('Enter the size of the linked list:- '))
        arr1 = [int(x) for x in input('Enter the elements:- ').split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        res=deleteMid(ll.head)
        printList(res)