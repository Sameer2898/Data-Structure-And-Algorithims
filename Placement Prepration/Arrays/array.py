print('Array')
arr = list(map(int, input().split(',')))
print('Array is:-')
print(arr)
print('Adding to array:-')
num = int(input('Enter a element to add to array:- '))
arr.append(num)
print(f'Array after adding {num} array is:- {arr}')
print('Deleting an element from array:-')
num1 = int(input('Enter a index of element to delete from array:- '))
arr.remove(num)
print(f'After deleting {num1} array is:- {arr}')
print('Searching to array:-')
num3 = int(input('Enter element to search:- '))
for i in range(len(arr)):
    if(arr[i] == num3):
        print(f'Element Found at index {i}')
        break
    else:
        print('Element not Found')
        break