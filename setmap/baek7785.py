import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    name, typ = input().strip().split()
    if typ == 'enter':
        S.add(name)
    elif typ == 'leave':
        S.remove(name)

arr = list(S)
arr.sort(reverse=True)
for a in arr:
    print(a)