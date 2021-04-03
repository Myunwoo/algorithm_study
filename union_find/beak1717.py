#https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

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

def isSameParent(x, y):
    if find(x) == find(y):
        print("YES")
    else:
        print("NO")

for _ in range(m):
    operator, a, b = map(int, sys.stdin.readline().strip().split())
    if operator == 0:
        union(a, b)
    else:
        isSameParent(a, b)