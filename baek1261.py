#https://www.acmicpc.net/problem/9376
import sys
from collections import deque

t=int(sys.stdin.readline())
for _ in range(t):
    graph=[]
    h, w = map(int, sys.stdin.readline().split())
    for _ in range(h):
        