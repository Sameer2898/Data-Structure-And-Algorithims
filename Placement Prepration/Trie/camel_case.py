class TrieNode:
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
        self.d=[]
  
class Trie: 
    global d
    d=dict()
    def __init__(self): 
        self.root =TrieNode()
        
def cti(ch):
    return ord(ch)-ord('A')
    
def insert(root,key):
    for e in key:
        idx=cti(e)
        if idx>26:
            continue
        if not root.children[idx]:
            root.children[idx]=TrieNode()
        root=root.children[idx]
    root.d.append(key)
    root.isEndOfWord=True


def search(root, key):
    for e in key:
        idx=cti(e)
        if not root.children[idx]:
            print('No match found',end=' ')
            return
        root=root.children[idx]
    pall(root)

def pall(root):
    if not root:
        return
    if root.isEndOfWord:
        for e in sorted(root.d):
            print(e,end=' ')
    for i in range(26):
        pall(root.children[i])
        
def printAllWords(arr,strs):
    t = Trie()
    for s in arr:
        insert(t.root,s)
    search(t.root,strs)

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = input('Enter the elements of the array:- ').strip().split()
        pattern = input('Enter the pattern to find in the string:- ')
        printAllWords(arr,pattern)
        print()