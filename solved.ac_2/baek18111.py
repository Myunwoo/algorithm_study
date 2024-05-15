import sys
input = sys.stdin.readline

N, M, B = list(map(int, input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]

minTime = float('inf')
height = 0

# 땅의 높이 범위가 0~256이므로 브루트포스로 풀이 가능
for ground in range(257):
  # 제거할 블록의 수
  digBlock = 0
  # 추가할 블록의 수
  addBlock = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] > ground:
        digBlock += graph[i][j] - ground
      else:
        addBlock += ground - graph[i][j]
  
  # graph[i][j]를 ground로 만들기 위해서는, 보유한 블록 수가 필요 블록 수만큼은 필요함
  if (digBlock+B) - addBlock >= 0:
    t = (digBlock*2) + addBlock
    if t <= minTime:
      minTime = t
      height = ground

print(minTime, height)