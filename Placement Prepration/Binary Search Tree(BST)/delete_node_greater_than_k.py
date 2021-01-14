def deleteNode(root, X):
    if root == None:
        return None
    if root.data >= X:
        return deleteNode(root.left, X)
    else:
        root.right = deleteNode(root.right, X)
        return root
    
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data <= node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the tree:- '))
        arr = list(map(int, input('Enter the elements of the tree:- ').strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        root = deleteNode(root, int(input()))
        traverseInorder(root)
        print()