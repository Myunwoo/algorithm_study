#https://www.acmicpc.net/problem/2798

import sys

N, M = map(int, sys.stdin.readline().strip().split())

cards = list(map(int, sys.stdin.readline().strip().split()))

a, b, c = 0, 0, 0
max_sum = -1

for i in range(len(cards)):
    a = cards[i]
    for j in range(len(cards)):
        if j == i:
            continue
        b = cards[j]
        for k in range(len(cards)):
            if k == i or k == j:
                continue
            c = cards[k]

            if (a+b+c) <= M:
                max_sum = max(max_sum,(a+b+c))

print(max_sum)