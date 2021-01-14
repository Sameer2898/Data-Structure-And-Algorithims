def inorder(root, dict1):
    if root == None:
        return 
    inorder(root.left, dict1)
    if root.left != None or root.right != None:
        if root.data in dict1:
            dict1[root.data].append(root)
        else:
            temp = []
            temp.append(root)
            dict1[root.data] = temp
    inorder(root.right, dict1)

def issub(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data == root2.data:
        return issub(root1.left, root2.left) and issub(root1.right, root2.right)
    else:
        return False
        
def dupSub(node):
    dict1 = {}
    inorder(node, dict1)
    duppres = False
    for x in dict1:
        if len(dict1[x]) > 1:
            for i in range(len(dict1[x])):
                for j in range(len(dict1[x])):
                    if i != j and issub(dict1[x][i], dict1[x][j]):
                        duppres = True
            if duppres:
                break
    if duppres:
        return 1
    else:
        return 0
    
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def __init__(self):
        self.j = 0
        
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            return self.insert(node.left, data)
        else:
            return self.insert(node.right, data)

    def insertString(self, node, string):
        if self.j > len(string):
            return None

        if string[self.j] == '(':
            self.j += 1

        if string[self.j] != '(' and string[self.j]!=')':
            node = self.insert(node, string[self.j])
            self.j += 1
            if string[self.j] == ')':
                return node

        if string[self.j] == '(':
            self.j += 1

        if string[self.j] == ')':
            node.left = None
        else:
            node.left = self.insertString(node.left, string)

        while string[self.j] == ')':
            self.j += 1
        if string[self.j] == '(':
            self.j += 1
        if string[self.j] == ')':
            node.right = None
            self.j += 1
        else:
            node.right = self.insertString(node.right, string)
        return node

    def printTree(self, node):
        if node is None:
            return None
        self.printTree(node.left)
        print(node.data, end=" ")
        self.printTree(node.right)

if __name__=='__main__':
    t = int(input('Enter the number of test cases:- '))
    for i in range(t):
        root = None
        tre = Tree()
        string = input('Enter the elements of the tree:- ').strip()
        root = tre.insertString(root, string)
        # tre.printTree(root)
        # print ''
        print(dupSub(root))