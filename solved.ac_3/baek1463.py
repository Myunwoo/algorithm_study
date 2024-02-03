from collections import deque
X = int(input())
dq = deque()
dq.append((X, 0))
answer = float('inf')

while dq:
  curX, curCount = dq.popleft()
  
  if curX%3 == 0:
    one = curX/3
    if one > 1:
      dq.append((one, curCount+1))
    elif one == 1:
      answer = min(answer,curCount+1)
  if curX%2 == 0:
    two = curX/2
    if two > 1:
      dq.append((two, curCount+1))
    elif two == 1:
      answer = min(answer,curCount+1)
  if curX > 1:
    three = curX-1
    if three == 1:
      answer = min(answer,curCount+1)
    dq.append((three, curCount+1))

print(answer)