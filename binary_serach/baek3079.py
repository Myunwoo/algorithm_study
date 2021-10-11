#https://www.acmicpc.net/problem/3079
import sys
N,M=map(int, sys.stdin.readline().split())
times=[]
for _ in range(N):
    times.append(int(sys.stdin.readline()))

#최소 몇 분이 걸릴까?에서 이 시간안에 몇 명까지 가능할까?로 문제를 바꿈
#이분탐색을 통해 M명을 심사할 수 있는 최소의 시간을 찾는다.
l=1
r=max(times)*M

def calcMaxPeople(m):
    global times
    result=0
    for t in times:
        result+=m//t
    return result

result=0
while l<=r:
    mid=(l+r)//2
    mp=calcMaxPeople(mid)
    if mp>=M:
        result=mid
        r=mid-1
    else:
        l=mid+1

print(result)