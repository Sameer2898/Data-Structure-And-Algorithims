from itertools import combinations

num = list(map(int, input().split()))
pos = int(input('Enter the position from where you find the combination:-'))
prem = combinations(num, pos)
print(f'The list is:- {num}.')
print(f'Combinations of {num} is:-')
for i in prem:
    print(i)