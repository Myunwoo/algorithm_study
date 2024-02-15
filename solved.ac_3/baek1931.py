import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:[x[1], x[0]])

stack = []
stack.append(arr[0])

for i in range(1, len(arr)):
  if arr[i][0] >= stack[-1][1]:
    stack.append(arr[i])
print(len(stack))