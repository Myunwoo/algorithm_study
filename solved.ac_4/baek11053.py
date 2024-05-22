N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

# i 번째 수 까지의 부분수열의 길이를 구하기 위해 순회
for i in range(1, N):
    # 0 ~ i-1 번쨰까지 순회
    for j in range(i):
        if A[j] < A[i]:
            # i 번째 수에 저장될 값은 i 이전까지 만들어졌던 최대 길이의 부분 수열의 길이
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))