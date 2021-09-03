#https://www.acmicpc.net/problem/14891
import sys
from collections import deque
t=[]
for _ in range(4):
    t.append(deque(list(sys.stdin.readline().strip())))
K=int(sys.stdin.readline())
for _ in range(K):
    num,direction=map(int, sys.stdin.readline().split())
    i=0
    ltargets=[]
    while True:
        #왼쪽 톱니바퀴가 존재하는 경우
        if num-(2+i)>=0:
            #왼쪽 톱니바퀴와 지정된 톱니바퀴의 극이 다른 경우
            if t[num-(2+i)][2] != t[num-(1+i)][6]:
                ltargets.append(num-(2+i))
            else:
                break
        else:
            break
        i+=1
    i=0
    rtargets=[]
    while True:
        #오른쪽 톱니바퀴가 존재하는 경우
        if (num+i)<=3:
            #오른쪽 톱니바퀴와 지정된 톱니바퀴의 극이 다른 경우
            if t[num+i][6] != t[num-1+i][2]:
                rtargets.append(num+i)
            else:
                break
        else:
            break
        i+=1

    #시계 방향으로 돌리는 경우
    if direction==1:
        t[num-1].appendleft(t[num-1].pop())

    #반시계 방향으로 돌리는 경우
    elif direction==-1:
        t[num-1].append(t[num-1].popleft())

    td=direction
    for target in ltargets:
        td*=-1
        if td==-1:
            t[target].append(t[target].popleft())
        else:
            t[target].appendleft(t[target].pop())
    td=direction
    for target in rtargets:
        td*=-1
        if td==-1:
            t[target].append(t[target].popleft())
        else:
            t[target].appendleft(t[target].pop())

score=0
for i in range(len(t)):
    if t[i][0]=='1':
        if i==0:
            score+=1
        elif i==1:
            score+=2
        elif i==2:
            score+=4
        elif i==3:
            score+=8

print(score)