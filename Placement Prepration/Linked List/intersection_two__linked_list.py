import atexit
import io
import sys

def get_size(head):
    ret = 0
    while head is not None:
        head = head.next
        ret += 1
    return ret

def intersetPoint(head_a,head_b):
    n1 = get_size(head_a)
    n2 = get_size(head_b)
    
    while n1 > n2:
        head_a = head_a.next
        n1 -= 1
    
    while n2 > n1:
        head_b = head_b.next
        n2 -= 1
    
    while head_a != head_b:
        head_a = head_a.next
        head_b = head_b.next
    
    if head_a is not None:
        return head_a.data
    return -1

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for cases in range(t):
        x,y,z = map(int,input('Enter the size of the linked list:- ').strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input('Enter the elements of the first linked list:- ').strip().split()))
        nodes_b = list(map(int, input('Enter the elements of the second linked list:- ').strip().split()))
        nodes_common = list(map(int, input('Enter the element whose intersection point is to be found:- ').strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))