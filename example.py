#https://www.acmicpc.net/problem/2579

import sys
N = int(input())
steps = []
for _ in range(N):
    steps.append(int(sys.stdin.readline().strip()))

scores = []

def dp():
