import heapq
from collections import deque

N = int(input())
ans = []
for _ in range(N):
  N, M = list(map(int, input().split()))
  costArr = list(map(int, input().split()))
  sortedArr = sorted(costArr)
  costArr = deque([(v, i) for i, v in enumerate(costArr)])
  count = 0

  while sortedArr:
    curCost = sortedArr.pop()
    while curCost != costArr[0][0]:
      costArr.append(costArr.popleft())
    count += 1
    now = costArr.popleft()
    if now[1] == M:
      break
  ans.append(count)

for a in ans:
  print(a)