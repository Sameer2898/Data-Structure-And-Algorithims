def printlist(node):
    if (node == None):
        return None
    ptr = node
    while ptr is not None:
        print(ptr.data, end=' ')
        ptr = ptr.next

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        llist = Linked_List()
        n = int(input('Enter the size of the linked list:- '))
        values = list(map(int, input('Enter the elements:- ').strip().split()))
        for i in values:
            llist.insert(i)
        printlist(llist.get_head())
        print('')