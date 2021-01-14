import atexit
import io
import sys

def fractionalknapsack(w,items,n):
    curr_weight = 0
    curr_value = 0
    items = sorted(items, key = lambda x: (x.value/x.weight), reverse = True)
    for i in range(n):
        if curr_weight + items[i].weight <= w:
            curr_weight += items[i].weight
            curr_value += items[i].value
        else:
            accomodate = w - curr_weight
            value_added = items[i].value * (accomodate/items[i].weight)
            curr_value += value_added
            break
    return curr_value

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases:- '))
    for cases in range(test_cases) :
        n,W = map(int,input('Enter the size and the maximum weight of the knapsack:- ').strip().split())
        info = list(map(int,input('Enter the elements of the knapsack:- ').strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        print("%.2f" %fractionalknapsack(W,Items,n))