def find_key(root, k, gt):
    if root == None:
        return gt
    if root.data > k:
        if root.left == None:
            return gt
        return max(gt, find_key(root.left, k, gt))
    elif root.data == k:
        return k
    else:
        if root.right == None:
            return root.data
        return find_key(root.right, k, root.data)
        
def findMaxforKey(root,k):
    if root.data == k:
        print(k)
    elif root.data < k:
        print(find_key(root, k, root.data))
    else:
        print(find_key(root, k, -1))

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    
    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node
            
    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
        
if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the tree:- '))
        arr = input('Enter the elements of the tree:- ').strip().split()
        
        tree = Tree()
        root = None
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
    
        num = int(input('Enter the number to find in the tree:- '))
        findMaxforKey(root,num)