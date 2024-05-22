from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

cols = list(combinations(arr, M))
for c in cols:
    c = str(c)
    c = c.replace('(', '')
    c = c.replace(')', '')
    c = c.replace(',', '')
    print(c)