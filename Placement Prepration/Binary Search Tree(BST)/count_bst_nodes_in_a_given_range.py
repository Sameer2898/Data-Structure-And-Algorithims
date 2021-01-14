def total(root, l, h):
    if root is None:
        return 0
    count = 0
    if root.data >= l and root.data <= h:
        count += 1
    return count + total(root.left, l, h) + total(root.right, l, h)
    
def getCountOfNode(root,l,h):
    if root is None:
        return 0
    return total(root, l, h)

class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp = Node()
    temp.data = value
    temp.left = None
    temp.right = None
    return temp
    
def newNode(root,data):
    if(root is None):
        root = createNewNode(data)
    elif(data<root.data):
        root.left = newNode(root.left,data);
    else:
        root.right = newNode(root.right,data)
        
    return root
    
def main():
    testcases = int(input('Enter the number of test cases:- '))
    while(testcases>0):
        root = None
        sizeOfArray = int(input('Enter the size of the tree:- '))
        arr = [int(x) for x in input('Enter the elements of the tree:- ').strip().split()]
        for i in arr:
            root = newNode(root,i)
            
        lr = [int(x) for x in input('Enter the range to find the elements in the tree:- ').strip().split()]

        print(getCountOfNode(root,lr[0],lr[1]))
        testcases -= 1

if __name__=="__main__":
    main()