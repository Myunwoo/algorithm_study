#https://www.acmicpc.net/problem/2217

import sys
N = int(sys.stdin.readline().strip())
ropes = [int(sys.stdin.readline().strip()) for _ in range(N)]

ropes.sort()
weight = [0 for _ in range(N)]
for i in range(N):
    weight[i] = ropes[i] * (N-i)

print(max(weight))