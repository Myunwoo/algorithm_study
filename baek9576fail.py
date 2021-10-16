#https://www.acmicpc.net/problem/9576
import sys
T=int(sys.stdin.readline())
results=[]
for _ in range(T):
    N,M=map(int, sys.stdin.readline().split())
    students=[]
    for _ in range(M):
        students.append(list(map(int, sys.stdin.readline().strip().split())))
    students.sort(key=lambda x:[x[0],x[1]],reverse=True)
    count=1
    m=students.pop()[0]

    while students:
        #끝점이 m보다 큰 것이 나올 때까지 계속 뽑음(끝이 m보다 커야 책을 줄 가능성이 있는 거니까)
        t=students.pop()
        if t[1]<=m:
            continue
        #뽑은 것의 시작점을 m과 비교
        if t[0]<=m:
            m+=1
            count+=1
        else:
            m=t[0]
            count+=1
    results.append(count)

for r in results:
    print(r)