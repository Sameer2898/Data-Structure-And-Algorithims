import atexit
import io
import sys

def getParent(x):  
    return (x - 1) // 2


def leftChild(x):
    return (2 * x + 1) if (2 * x + 1) < curr_size else -1

def rightChild(x): 
    return (2 * x + 2) if (2 * x + 2) < curr_size else -1

def heapify():
    curr_ind = curr_size - 1
    while getParent(curr_ind) != -1 and heap[getParent(curr_ind)] > heap[curr_ind]:
        heap[curr_ind], heap[getParent(curr_ind)] = heap[getParent(curr_ind)], heap[curr_ind]
        curr_ind = getParent(curr_ind)
    return

def heapifyDown(x):
    if x >= curr_size: 
        return
    if getParent(x) != -1 and heap[x] < heap[getParent(x)]:
        heap[x], heap[getParent(x)] = heap[getParent(x)], heap[x]
        heapifyDown(getParent(x))
    if leftChild(x)==-1 or (leftChild(x)!=-1 and heap[x]<heap[leftChild(x)]):
        if rightChild(x)==-1 or (rightChild(x)!=-1 and heap[x]<heap[rightChild(x)]):
            return  
    if rightChild(x)==-1:
        heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
        heapifyDown(leftChild(x))
    elif leftChild(x) == -1:
        heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
        heapifyDown(rightChild(x))
    else:  
        if heap[rightChild(x)]<heap[leftChild(x)]:
            heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
            heapifyDown(rightChild(x))
        else:
            heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
            heapifyDown(leftChild(x))
    return


def insertKey (x):
    global curr_size
    heap[curr_size] = x
    curr_size += 1
    heapify()

def deleteKey (x):
    global curr_size
    if x >= curr_size:  
        return
    heap[x] = heap[curr_size - 1]
    heap[curr_size - 1] = 0 
    curr_size -= 1 
    heapifyDown(x) 

def extractMin ():
    if curr_size == 0:
        return -1
    val = heap[0]
    deleteKey(0) 
    return val

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input('Enter the numbr of test cases:- '))
    for cases in range(test_cases):
        n = int(input('Enter the size of the heap:- '))
        a = list(map(int, input('Enter the elements of the heap:- ').strip().split()))
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        print()