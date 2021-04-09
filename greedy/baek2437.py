#https://www.acmicpc.net/problem/2437

N = int(input())
plumbs = list(map(int, input().split()))

plumbs.sort()

target = 1
for plumb in plumbs:
    if target < plumb:
        break
    target += plumb

print(target)