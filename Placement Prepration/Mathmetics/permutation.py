from itertools import permutations

num = list(map(int, input().split()))
prem = permutations(num)
print(f'The list is:- {num}.')
print(f'Permutations of {num} is:-')
for i in prem:
    print(i)