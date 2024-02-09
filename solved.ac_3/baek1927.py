import heapq
answer = []
N = int(input())
heap = []
for _ in range(N):
  x = int(input())
  if x > 0:
    heapq.heappush(heap, x)
  elif x == 0:
    if heap:
      answer.append(heapq.heappop(heap))
    else:
      answer.append(0)

for a in answer:
  print(a)