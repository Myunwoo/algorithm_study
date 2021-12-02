#https://www.acmicpc.net/problem/20165
import sys
N,M,R=map(int, sys.stdin.readline().split())
graph=[]
domino=[['S' for _ in range(M)] for _ in range(N)]
score=0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))


def fall(x,y,d):
    global score
    h=graph[x][y]
    nx=x
    ny=y
    #이것때문에 시간 오지게버림
    #시작지점 쓰러트려줌
    #domino[nx][ny]='F'
    #언제까지 넘어뜨릴까 반복해서 찾아내기
    while h:
        #맵 밖인 경우엔 그만둠
        if nx<0 or nx>=N or ny<0 or ny>=M:
            break
        #서있을 경우에 점수 올리고 최대높이 갱신
        if domino[nx][ny] == 'S':
            domino[nx][ny]='F'
            score+=1
            h=max(h,graph[nx][ny])
        #다음 지점은 방향이 결정
        if d == 'E':
            ny+=1
        elif d=='W':
            ny-=1
        elif d=='S':
            nx+=1
        elif d=='N':
            nx-=1
        #한 칸 뿌쉈으니까 높이 1감소
        h-=1


for _ in range(R):
    attack=list(sys.stdin.readline().strip().split())
    deffence=list(map(int,sys.stdin.readline().strip().split()))

    if domino[int(attack[0])-1][int(attack[1])-1] == 'S':
        fall(int(attack[0])-1,int(attack[1])-1,attack[2])
    domino[int(deffence[0])-1][int(deffence[1])-1]='S'

print(score)
for dom in domino:
    for d in dom:
        print(d, end=' ')
    print()