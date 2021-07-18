#https://www.acmicpc.net/problem/1261
import sys
from heapq import heappush, heappop
M, N = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))

costs=[[0 for _ in range(M)] for _ in range(N)]
heap=[]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dijkstra():
    global graph, costs, heap, dx, dy
    