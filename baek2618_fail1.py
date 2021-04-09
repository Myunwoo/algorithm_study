#https://www.acmicpc.net/problem/2618

import sys

N = int(sys.stdin.readline().strip())
W = int(sys.stdin.readline().strip())

accidents = []
pol1 = (1,1)
pol2 = (N,N)

sumOfRoads = 0
polArr = []

for _ in range(W):
    r, c = map(int, sys.stdin.readline().strip().split())
    accidents.append((r, c))

def arrangePol(accident):
    global pol1
    global pol2
    global sumOfRoads
    global polArr

    #pol1과 pol2모두에서 accident까지 가는 길이를 구함.
    pol1Cost = abs(pol1[0] - accident[0]) + abs(pol1[1] - accident[1])
    pol2Cost = abs(pol2[0] - accident[0]) + abs(pol2[1] - accident[1])
    
    #그 중 짧은 길이를 택해서 맡은 경찰의 번호를 배열에 저장, 길이를 길이합산 변수에 합산
    #이동한 pol튜플의 값을  accident로 세팅해줌.
    #이 풀이에서는 그저 가까운 경찰차의 위치만을 생각했음! 그런데 경찰차의 총 이동거리 수가 최소이려면 때로는 먼 곳의 경찰차를 당겨올 일도 생김!
    if pol1Cost >= pol2Cost:
        polArr.append(2)
        sumOfRoads += pol2Cost
        pol2 = accident
    else:
        polArr.append(1)
        sumOfRoads += pol1Cost
        pol1 = accident


for accident in accidents:
    arrangePol(accident)

print(sumOfRoads)
for pol in polArr:
    print(pol)