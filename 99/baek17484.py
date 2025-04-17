import sys
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[[sys.maxsize] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    dp[0][i] = [graph[0][i], graph[0][i], graph[0][i]]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 2) or (j==M-1 and k == 0):
                continue
            for l in range(3):
                # 같은 방향으로 이동 불가
                if k == l:
                    continue
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-k+1][l] + graph[i][j])

answer = sys.maxsize
for d in dp[-1]:
    answer = min(answer, min(d))

print(answer)