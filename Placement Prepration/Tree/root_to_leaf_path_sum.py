def hasPathSum(node, sm):
    if node is None:
        return (sm == 0)
    else:
        ans = 0
        subsum = sm - node.data
        if (subsum == 0 and node.left == None and node.right == None):
            return True
        if node.left is not None:
            ans = ans or hasPathSum(node.left, subsum)
        if node.right is not None:
            ans = ans or hasPathSum(node.right, subsum)
        return ans

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
    
    
if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases):
        s = input('Enter the element of the tree:- ')
        root = buildTree(s)
        sum = int(input('Enter the number say sum:- '))
        if hasPathSum(root, sum)==True:
            print(1)
        else:
            print(0)