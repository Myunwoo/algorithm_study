T = int(input())
answer = []

for _ in range(T):
  M, N, x, y = list(map(int, input().split()))
  curX, curY = 1, 1
  if x==1 and y==1:
    answer.append(1)
    continue
  
  count = 1
  found = False
  while True:
    curX += 1
    curY += 1
    count += 1
    if curX > M:
      curX = 1
    if curY > N:
      curY = 1

    if curX == x and curY == y:
      found = True
      answer.append(count)
      break
    if curX == M and curY == N:
      break
  if not found:
    answer.append(-1)

for a in answer:
  print(a)