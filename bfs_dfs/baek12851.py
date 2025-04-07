from collections import deque
N, K = map(int, input().split())

costs = [float('inf') for _ in range(100001)]
costs[N] = 0
dq = deque()
dq.append(N)
result = 0
count = 0

while dq:
  cur = dq.popleft()
  curCost = costs[cur]
  if cur == K:
    result = curCost
    count += 1

  for new in [cur+1, cur-1, cur*2]:
    if 0<= new < 100001 and costs[new] >= curCost+1:
      dq.append(new)
      costs[new] = curCost+1

print(result)
print(count)