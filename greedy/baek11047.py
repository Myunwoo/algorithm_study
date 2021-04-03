import sys

N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()

count = 0

for coin in coins:
    count += K // coin
    K -= (K // coin) * coin

print(count)