import sys
sys.setrecursionlimit(100)
# sys.setrecursionlimit(1000000)

def merge(first, second):
    if first is None:
        return second
    if second is None:
        return first
    if first.data < second.data:
        first.next = merge(first.next, second)
        first.next.prev = first
        first.prev = None
        return first
    else:
        second.next = merge(first, second.next)
        second.next.prev = second
        second.prev = None
        return second
    
def sortDoubly(head):
    if head is None:
        return head
    if head.next is None:
        return head
    second = split(head)
    head = sortDoubly(head)
    second = sortDoubly(second)
    return merge(head, second)

def split(head):
    fast = slow = head
    while(True):
        if fast.next is None:
            break
        if fast.next.next is None:
            break
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    return temp

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
        new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node
		
	def printList(self, node):
		while(node.next is not None):
			node = node.next
		while node.prev is not None:
		    node = node.prev
		while(node is not None):
		    print(node.data, end=" ")
		    node = node.next
		print()
    
def printList(node): 
        temp = node 
      
        while(node is not None): 
            print (node.data,end=" ")
            temp = node 
            node = node.next
        print()
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.prev 

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the linked list:- '))
        arr = list(map(int, input('Enter the element of the linked list:- ').strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        llist.head=sortDoubly(llist.head)
        printList(llist.head)
        print()
