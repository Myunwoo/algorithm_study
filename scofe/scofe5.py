from collections import deque

N, M = map(int, input().split())

matrix = []
starts = []
solutions = []

dr = [1, 0, 0]
dc = [0, 1, -1]

def dfs(start_c):
    global matrix
    global solutions
    global dq
    counts = []
    count = 0
    dq.append((0, start_c))

    while dq:
        p = dq.pop()
        curR = p[0]
        curC = p[1]
        if curR == M-1 and matrix[curR][curC] == '.':
            counts.append(count)
            count=0
        
        for i in range(3):
            nextR = curR + dr[i]
            nextC = curC + dc[i]

            if nextC < 0 or nextC >= N or nextR >= M:
                continue

            if i == 0 and matrix[nextR][nextC] == '.':
                #만약 바로 내려갈 길이 있다면 내려감.
                dq.appendleft((nextR, nextC))
                break
            
            if matrix[nextR][nextC] == '.':
                #좌, 우 이동에 해당하므로 카운팅
                count+=1
                dq.appendleft((nextR, nextC))
    
    counts.sort()
    return counts[0]

            

#맵 입력받고 시작점 저장
for i in range(M):
    matrix.append(list(input()))
    if i == 0:
        for index in range(N):
            if matrix[0][index] == 'c':
                starts.append(index)

while starts:
    #시작점 한 개 마다 dfs수행
    dq = deque()
    dfs(starts.pop())