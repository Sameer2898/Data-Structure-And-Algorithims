def kthancestor(root, val, stack):
    if root == None:
        return False
    if root.data == val:
        return True
    stack.append(root.data)
    left = kthancestor(root.left, val, stack)
    right = kthancestor(root.right, val, stack)
    if left or right:
        return True
    else:
        stack.pop()
        return False
        
def kthAncestor(root,k, node):
    stack = deque()
    kthancestor(root, node, stack)
    if k > len(stack):
        return -1
    else:
        temp = 0
        while k > 0:
            temp = stack.pop()
            k = k - 1
        return temp

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(0, t):
        k, node = [int(x) for x in input().split()]
        s = input('Enter the elements of the tree:- ')
        root = buildTree(s)
        print(kthAncestor(root,k,node))