#https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline().strip())
steps = []
for _ in range(n):
    steps.append(int(sys.stdin.readline().strip()))

costs = []
costs.append(steps[0])
if n >= 2:
    costs.append(steps[0]+steps[1])
if n>= 3:
    costs.append(max(steps[1]+steps[2], steps[0]+steps[2]))

if n>= 3:
    for i in range(3, n):
        costs.append(max(costs[i-3]+steps[i-1]+steps[i], costs[i-2]+steps[i]))

print(costs[len(costs)-1])