N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

for i in range(len(arr)):
  w, h = arr[i]
  count = 0
  for j in range(len(arr)):
    if i==j:
      continue
    cw, ch = arr[j]
    if cw > w and ch > h:
      count += 1
  print(count+1, end=' ')