import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [['.', '.'] for _ in range(N)]

for _ in range(N):
    root, left, right = map(lambda x:(ord(x)-65) if x != '.' else '.', input().strip().split())
    if left != '.':
        graph[root][0] = left
    if right != '.':
        graph[root][1] = right

fistRoute = ''
# 전위 순회
def first(cur):
    global fistRoute
    fistRoute += chr(65+cur)
    if graph[cur][0] != '.':
        first(graph[cur][0])
    if graph[cur][1] != '.':
        first(graph[cur][1])

midRoute = ''
# 중위 순회
def mid(cur):
    global midRoute
    if graph[cur][0] != '.':
        mid(graph[cur][0])
    midRoute += chr(65+cur)
    if graph[cur][1] != '.':
        mid(graph[cur][1])

lastRoute = ''
# 후위 순회
def last(cur):
    global lastRoute
    if graph[cur][0] != '.':
        last(graph[cur][0])
    if graph[cur][1] != '.':
        last(graph[cur][1])
    lastRoute += chr(65+cur)

first(0)
print(fistRoute)
mid(0)
print(midRoute)
last(0)
print(lastRoute)