#https://www.acmicpc.net/problem/9576
import sys
T=int(sys.stdin.readline())
results=[]

for _ in range(T):
    N,M=map(int, sys.stdin.readline().split())
    visited=[False for _ in range(N+1)]
    students=[]
    count=0
    for _ in range(M):
        students.append(list(map(int, sys.stdin.readline().strip().split())))
    students.sort(key=lambda x:x[1],reverse=True)

    while students:
        s=students.pop()
        for i in range(s[0],s[1]+1):
            if not visited[i]:
                count+=1
                visited[i]=True
                break
    results.append(count)

for r in results:
    print(r)