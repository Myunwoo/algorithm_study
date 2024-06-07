dp = dict()

def fibo(n):
      if dp.get(n) != None:
            return dp[n]
      if n == 0:
            return 0
      if n == 1 or n == 2:
            return 1
      if n % 2 == 0:
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007 # 맨 처음에는 % 1000000007을 해주지 않아 시간초과가 났었다..
            dp[n // 2 - 1] = fibo(n // 2 - 1) % 1000000007
            return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
      else:
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
            dp[n // 2] = fibo(n // 2) % 1000000007
            return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

print(fibo(int(input())) % 1000000007)