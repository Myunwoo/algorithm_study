#https://www.acmicpc.net/problem/11053
N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))