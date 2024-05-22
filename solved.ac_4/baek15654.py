from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

combs = list(permutations(arr, M))
for c in combs:
    c = str(c)
    c = c.replace('(', '')
    c = c.replace(')', '')
    c = c.replace(',', '')
    print(c)