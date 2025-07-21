import sys
N = int(sys.stdin.readline())
timeArr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
timeArr.sort(key=lambda x: [x[1], x[0]])

answer = 0
curTime = 0

for startTime, endTime in timeArr:
  # 진행할 수 있는 회의
  if startTime >= curTime:
    answer += 1
    curTime = endTime

print(answer)