from collections import deque
N, K = list(map(int, input().split()))
arr = [0 for _ in range(100001)]
dq = deque()
dq.append(N)
while dq:
  curP = dq.popleft()
  if curP == K:
    print(arr[curP])
    break
  for newP in (curP+1, curP-1, curP*2):
    if 0 <= newP <= 100000 and not arr[newP]:
      arr[newP] = arr[curP] + 1
      dq.append(newP)