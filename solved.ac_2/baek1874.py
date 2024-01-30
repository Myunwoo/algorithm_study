import sys
input = sys.stdin.readline
n = int(input())
arr = []
count = 1
answer = []
right = True

for _ in range(n):
    cur = int(input())
    if not right:
        continue
    while count <= cur:
        arr.append(count)
        count += 1
        answer.append('+')
    if arr[-1] == cur:
        arr.pop()
        answer.append('-')
    else:
        right = False

if right:
    for a in answer:
        print(a)
else:
    print('NO')