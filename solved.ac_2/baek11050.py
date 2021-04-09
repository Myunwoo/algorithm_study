#https://www.acmicpc.net/problem/11050

from math import factorial

N, K = map(int, input().split())

cnk = factorial(N) // (factorial(K) * factorial(N - K))
print(cnk)