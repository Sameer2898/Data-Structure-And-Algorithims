import heapq

def decodeHuffmanData(root, binaryString):
    ans = ''
    curr = root
    for i in range(len(binaryString)):
        if binaryString[i] == '0':
            curr = curr.left
        else:
            curr = curr.right
        if(curr.left == None and curr.right == None):
            ans += curr.data
            curr = root
    return ans

minheap = []
heapq.heapify(minheap)
cnt=0
codes = {}
freq = {}

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

def printCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        print(str(root.data)+": "+strr)
    printCodes(root.left, strr+"0")
    printCodes(root.right, strr+"1")

def storeCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        codes[root.data]=strr
    storeCodes(root.left, strr+"0")
    storeCodes(root.right, strr+"1")

def huffmanCodes(s):
    global cnt
    for v in freq:
        heapq.heappush(minheap, (freq[v], freq[v]+cnt, MinHeapNode(v, freq[v])))
        cnt+=1
    while(len(minheap) is not 1):
        left = minheap[0][2]
        heapq.heappop(minheap)
        right = minheap[0][2]
        heapq.heappop(minheap)
        top = MinHeapNode('$', left.freq+right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minheap, (top.freq, top.freq+cnt, top))
        cnt+=1
    storeCodes(minheap[0][2], "")


def calcFreq(strr, n):
    for i in range(n):
        if strr[i] not in freq:
            freq[strr[i]]=1
        else:
            freq[strr[i]]+=1


if __name__ == "__main__":
    t = int(input('Enter the number of test cases:- '))
    while(t>0):
        strr = input('Enter the string:- ')
        encodedString = ""
        decodedString = ""
        calcFreq(strr, len(strr))
        #print(freq)
        huffmanCodes(len(strr))
        #print(codes)
        for i in strr:
            encodedString += codes[i]

        decodedString = decodeHuffmanData(minheap[0][2], encodedString)
        print(decodedString)
        t=t-1