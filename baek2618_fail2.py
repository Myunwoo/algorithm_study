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

def arrangePol(index):
    global pol1
    global pol2
    global sumOfRoads
    global polArr
    global accidents

    #현재 pol1의 위치에서 사건까지의 거리
    pol1Cost = abs(pol1[0] - accidents[index][0]) + abs(pol1[1] - accidents[index][1])
    #현재 pol2의 위치에서 사건까지의 거리
    pol2Cost = abs(pol2[0] - accidents[index][0]) + abs(pol2[1] - accidents[index][1])

    #현재 사고에서 다음 사고까지의 거리
    if index >= len(accidents)-1:
        acciCost = 0
    else:
        acciCost = abs(accidents[index][0] - accidents[index+1][0]) + abs(accidents[index][1] - accidents[index+1][1])

    if (pol1Cost + acciCost) >= (pol2Cost + acciCost):
        sumOfRoads += pol2Cost
        pol2 = accidents[index]
        polArr.append(2)
        print("po1: " + str(pol1) + ", pol2: " + str(pol2))
        print("sumOfRoads: " + str(sumOfRoads))
    else:
        sumOfRoads += pol1Cost
        pol1 = accidents[index]
        polArr.append(1)
        print("po1: " + str(pol1) + ", pol2: " + str(pol2))
        print("sumOfRoads: " + str(sumOfRoads))
    
    
for index in range(len(accidents)):
    arrangePol(index)

print(sumOfRoads)
for pol in polArr:
    print(pol)