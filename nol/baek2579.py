import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    print(arr[0])
    exit()
elif N == 2:
    print(arr[0]+arr[1])
    exit()
elif N == 3:
    print(max(arr[0]+arr[2], arr[1]+arr[2]))
    exit()

dp = [0 for _ in range(N)]
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, N):
    dp[i] = arr[i] + max(dp[i-2], dp[i-3]+arr[i-1])

print(dp[-1])