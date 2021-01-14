def cti(ch):
    return ord(ch) - ord('a')
    
def insert(root,key):
    for e in key:
        idx = cti(e)
        if not root.children[idx]:
            root.children[idx] = TrieNode()
        root = root.children[idx]
    root.isEndOfWord = True

def search(root, key):
    for e in key:
        idx = cti(e)
        if not root.children[idx]:
            return
        root = root.children[idx]
    return root.isEndOfWord

class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t = int(input('Enter the number of test cases:- '))
    for tcs in range(t):
        n = int(input('Enter the size of the array:- '))
        arr = input('Enter the elements:- ').strip().split()
        strs = input('Enter the word to be search:- ')
        t = Trie()
        for s in arr:
            insert(t.root,s)
        if search(t.root,strs):
            print(1)
        else:
            print(0)