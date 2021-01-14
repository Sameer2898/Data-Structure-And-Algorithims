def buildBalancedTree(root): 
    inorder = []
    def recurse(node):
        if node.left:
            recurse(node.left)
        inorder.append(node.data)
        if node.right:
            recurse(node.right)
            
    def construct(low, high):
        if low > high:
            return None
            
        mid = (low + high)//2
        
        node = Node(inorder[mid])
        node.left = construct(low, mid-1)
        node.right = construct(mid+1, high)
        return node
        
    recurse(root)
    return construct(0, len(inorder)-1)

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
            
            

def height(root):
    if not root:
        return 0
    ldepth = height(root.left)
    rdepth = height(root.right)
    
    if ldepth>rdepth:
        return ldepth
    else:
        return rdepth+1
        

if __name__=='__main__':
    t=int(input('Enter the number of test cases:- '))
    for i in range(t):
        n = int(input('Enter the size of the tree:- '))
        arr = input('Enter the elements of the tree:- ').strip().split()

        tree = Tree()
        root = None
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        
        resRoot = buildBalancedTree(root)
        print(height(resRoot))