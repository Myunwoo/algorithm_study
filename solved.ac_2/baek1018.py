import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [list(input().strip()) for _ in range(N)]

minCount = float('inf')

for startN in range(N-7):
  for startM in range(M-7):
    countW, countB = 0, 0
    for i in range(8):
      for j in range(8):
        s = i+j
        if s % 2 == 0:
          if graph[i+startN][j+startM] != 'W':
            countW += 1
          else:
            countB += 1
        else:
          if graph[i+startN][j+startM] != 'B':
            countW += 1
          else:
            countB += 1
    minCount = min(minCount, countW, countB)

print(minCount)