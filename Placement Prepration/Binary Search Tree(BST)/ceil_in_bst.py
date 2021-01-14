import atexit
import io
import sys

def findCeil(root, inp):
    if root == None:
        return -1
    if root.key == inp:
        return root.key
    if root.key < inp:
        return findCeil(root.right, inp)
    val = findCeil(root.left, inp)
    if val >= inp:
        return val
    else:
        return root.key

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class:
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

# Tree Class
class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self,x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x: # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:   #  go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return # no duplicate is to be inserted

        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)
        return


if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        n = int(input('Enter the size of the tree:- '))  # number of nodes in tree
        a = list(map(int, input('Enter the elements of the tree:- ').strip().split()))  # parent child info in list
        x = int(input('Enter the element to be found in the tree:- '))
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        print(findCeil(tree.root,x))