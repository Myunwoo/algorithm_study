#https://www.acmicpc.net/problem/18808
import sys
N,M,K=map(int,sys.stdin.readline().split())
graph=[[0 for _ in range(M)] for _ in range(N)]
sticker=[]

# 시계방향으로 90도 회전한 배열을 반환한다.
def rotate_90(array):
    ver, hor = len(array), len(array[0])
    new_array = [[array[-j + ver - 1][i] for j in range(ver)] for i in range(hor)]
    return new_array

#실제로 스티커를 붙여보는 함수, 스티커를 붙일 수 있다면 True리턴하고 스티커를 graph에 붙여줌.
#못 붙이면 False리턴
def checkArea(startR,startC):
    global sticker
    for i in range(startR, startR+len(sticker)):
        for j in range(startC,startC+len(sticker[0])):
            if graph[i][j]==1 and sticker[i-startR][j-startC]==1:
                return False
    #스티커 붙이기
    for i in range(startR, startR+len(sticker)):
        for j in range(startC,startC+len(sticker[0])):
            if sticker[i-startR][j-startC]==1:
                graph[i][j]=1
    return True

#각 자리마다 4방향의 시도를 해야함. 스티커를 돌려가면서 시도하고, 붙일 수 있다면 true를, 없으면 false를 리턴
#startR,startC는 좌측상단의 점, stickerR,stickerC는 스티커의 크기
def checkAllDirections(startR,startC):
    global graph,sticker
    #4가지 방향
    for direction in range(4):
        if direction>0:
            rotate_90(sticker)
        #4가지 방향을 시도하고 붙일 수 있는 경우 True리턴
        if checkArea(startR,startC):
            return True
    return False

#sticker를 graph에 붙여볼 것. (N-R+1)*(M-C+1)번 loop를 돌며 그 자리에 스티커가 붙여질 수 있는지 확인
#스티커가 붙여진다면 sticker에 포함된 1의 개수를 리턴, 안 붙여진다면 0리턴
def postIt(R,C):
    global graph,N,M,sticker
    r=0
    #1 1 1 1 1
    #0 0 0 1 0
    #블록을 시도할 때, 블록이 맵 밖으로 나가는 문제 때문에 for문이 동작하지 않고 결국 어떠한 탐색도 이루어지지 않음
    for i in range(N-R+1):
        for j in range(M-C+1):
            if checkAllDirections(i,j):
                for s in sticker:
                    r+=sum(s)
                return r
    return r


result=0
for _ in range(K):
    R,C=map(int, sys.stdin.readline().split())
    for _ in range(R):
        sticker.append(list(map(int, sys.stdin.readline().strip().split())))
    result+=postIt(R,C)
    sticker=[]
    for g in graph:
        print(g)

print(result)