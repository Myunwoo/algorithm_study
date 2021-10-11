#https://www.acmicpc.net/problem/1184
import sys
N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

