import atexit
import io
import sys
from collections import  defaultdict

def createnode(parent, i, created, root):
    if created[i] is not None:
        return 
    created[i] = Node(i)
    if parent[i] == -1:
        root[0] = created[i]
        return
    if created[parent[i]] is None:
        createnode(parent, parent[i], created, root)
    p = created[parent[i]]
    if p.left is None:
        p.left = created[i]
    else:
        p.right = created[i]

def createTree(parent,n):
    n = len(parent)
    created = [None for i in range(n + 1)]
    root = [None]
    for i in range(n):
        createnode(parent, i, created, root)
    return root[0]

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function should print the level order of the tree in sorted format
def traverse_level_order(root):
    # Code here
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n == 0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes,end=" ")
        while(n > 0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n -= 1

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        n = int(input('Enter the size of the array:- '))  # number of nodes in tree
        a = list(map(int, input('Enter the elements of the array:- ').strip().split()))  # parent child info in list
        traverse_level_order(createTree(a,n))
        print()