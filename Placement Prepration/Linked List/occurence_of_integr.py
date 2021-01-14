class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.

def count(head, search_for):
    flag = head
    c = 0
    while flag is not None:
        if flag.data == search_for:
            c += 1
        flag = flag.next
    return c

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    t = int(input('Enter the number of test cases:- '))
    while (t > 0):
        llist = LinkedList()
        n = int(input('Enter the size of the linked list:- '))
        values = list(map(int, input('Enter the elements of the linked list:- ').split()))
        for i in reversed(values):
            llist.push(i)
        m = int(input())
        k = count(llist.head, m)
        print(k)
        t -= 1