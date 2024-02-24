N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]

answer = 0
while K > 0:
  c = coins.pop()
  if K // c >= 1:
    answer += K // c
    K %= c

print(answer)