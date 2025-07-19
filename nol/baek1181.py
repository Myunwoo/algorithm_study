import sys
N = int(sys.stdin.readline())
arr = []
answer = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())

arr.sort(key=lambda x:[len(x), x])

answer = [arr[0]]
for i in range(1, N):
    if answer[-1] == arr[i]:
        continue
    answer.append(arr[i])


for a in answer:
    print(a)