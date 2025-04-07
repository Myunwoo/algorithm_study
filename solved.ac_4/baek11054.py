N = int(input())
A = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i][0] = max(dp[j][0]+1, dp[i][0])

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            dp[i][1] = max(dp[j][1]+1, dp[i][1])

result = 0
for d in dp:
    result = max(result, sum(d))

print(result+1)