#https://www.acmicpc.net/problem/3020
import sys
N, H=map(int, sys.stdin.readline().split())
#석순
suks=[0 for _ in range(H+1)]
#종유석
jongs=[0 for _ in range(H+1)]

for i in range(N):
    length=int(sys.stdin.readline().strip())
    if i%2==0:
        suks[length]+=1
    else:
        jongs[length]+=1

#석순과 종유석의 누적합
for i in range(H-1,0,-1):
    suks[i]+=suks[i+1]
    jongs[i]+=jongs[i+1]

#최소 횟수가 등장한 횟수
count=0
#머리 박는 최소 횟수
huddle=N

#석순, 종유석의 길이는 1이상이기 때문에 1부터 탐색
for i in range(1,H+1):
    if huddle > (suks[i] + jongs[H-i+1]):
        huddle = suks[i] + jongs[H-i+1]
        count=1
    elif huddle==(suks[i] + jongs[H-i+1]):
        count+=1
        

print(huddle, count)