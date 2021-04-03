#https://www.acmicpc.net/problem/1976

import sys

N = int(sys.stdin.readline().strip())

parent = [i for i in range(N+1)]

M = int(sys.stdin.readline().strip())

#num이 어떤 집합에 포함되어 있는지 확인하는 함수
def find(c):
    if(parent[c] == c): 
        return c
    #이게 경로 최적화? 라고 하던데 무슨의미인지 모르겠습니다....ㅠ
    parent[c] = find(parent[c])
    return parent[c]

#두 수 x, y가 포함된 집합을 합치는 함수
def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        if x < y: 
            parent[y] = x
        else:
            parent[x] = y

for i in range(1, N+1):
    maps = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(1, len(maps)+1):
        #연결되야 할 두 점이라면 union으로 이어주기
        if maps[j-1] == 1:
            union(i, j)


plan = list(map(int, sys.stdin.readline().strip().split()))

result = set([find(i) for i in plan])
if len(result) != 1:
    print("NO")
else:
    print("YES")