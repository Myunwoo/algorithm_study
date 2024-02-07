from collections import deque
N, K = list(map(int, input().split()))
visited = [False for _ in range(100001)]
dq = deque()
answer = float('inf')

dq.append((N, 0))
while dq:
  curP, curTime = dq.popleft()
  if curP == K:
    answer = min(answer, curTime)

  new1 = curP+1
  if new1 <= 100000 and not visited[new1]:
    visited[new1] = True
    dq.append((new1, curTime+1))
  new2 = curP-1
  if new2 > 0 and not visited[new2]:
    visited[new2] = True
    dq.append((new2, curTime+1))
  new3 = curP*2
  if new3 <= 100000 and not visited[new3]:
    visited[new3] = True
    dq.append((new3, curTime+1))

print(answer)