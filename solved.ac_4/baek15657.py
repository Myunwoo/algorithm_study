from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

combs = list(combinations_with_replacement(arr, M))
for c in combs:
    c = str(c)
    c = c.replace('(', '')
    c = c.replace(')', '')
    c = c.replace(',', '')
    print(c)