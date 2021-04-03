#https://www.acmicpc.net/problem/1932

import sys

n = int(input())

stairs = []

for _ in range(n):
    stairs.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(len(stairs)-2, -1, -1):
    for j in range(len(stairs[i])):
        stairs[i][j] += max(stairs[i+1][j], stairs[i+1][j+1])

print(stairs[0][0])