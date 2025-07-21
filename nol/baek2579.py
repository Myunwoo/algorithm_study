import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * N

if N == 1:
    print(arr[0])
elif N == 2:
    print(sum(arr))
elif N == 3:
    print(max(arr[0]+arr[2], arr[1]+arr[2]))
else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
    for i in range(3, N):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(dp[-1])


