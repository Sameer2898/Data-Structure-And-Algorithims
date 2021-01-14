def deletebt(root, key):
    q = deque()
    q.append(root)
    prev = None
    keypoint = None
    while q:
        size = len(q)
        for i in range(0, size):
            curr = q.popleft()
            prev = curr
            if curr.data == key:
                keypoint = curr
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
    return [prev, keypoint]

def parent(root, prev):
    if root == None:
        return None
    if root.left == prev or root.right == prev:
        return root
    left = parent(root.left, prev)
    right = parent(root.right, prev)
    if left == None and right == None:
        return None
    elif left == None:
        return right
    else:
        return left

def deletionBT(root, key):
    arr = deletebt(root, key)
    prev = arr[0]
    keypoint = arr[1]
    if keypoint == None:
        return
    elif prev == keypoint:
        if prev == root:
            return root
        par = parent(root, prev)
        if par.left == prev:
            par.left = None
        if par.right == prev:
            par.right = None
    else:
        par = parent(root, prev)
        if par.left == prev:
            keypoint.data = prev.data
            par.left = None
        if par.right == prev:
            keypoint.data = prev.data
            par.right = None

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s) == 0 or s[0] == "N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip = list(map(str,s.split()))
    
    # Create the root of the tree
    root = Node(int(ip[0]))                     
    size = 0
    q = deque()
    
    # Push the root to the queue
    q.append(root)                            
    size = size+1 
    
    # Starting from the second element
    i = 1                                       
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if(currVal != "N"):
            
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if(currVal != "N"):
            
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)    
    
if __name__=="__main__":
    t = int(input('Enter the number of test cases:- '))
    for _ in range(0,t):
        key = int(input('Enter the key to be deleted:- '))
        s = input('Enter the element of the tree:- ')
        root = buildTree(s)
        deletionBT(root, key)
        inorder(root)
        print()