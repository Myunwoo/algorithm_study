#https://www.acmicpc.net/problem/1937
import sys
n=int(sys.stdin.readline())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip().split())))
panda=[[-1 for _ in range(n)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#x,y는 판다가 처음 가보는 길임이 보장됨.
def dfs(cur_x,cur_y):
    #print('dfs called:('+str(cur_x)+','+str(cur_y)+')')
    global graph,dx,dy
    moved=False

    for i in range(4):
        new_x=cur_x+dx[i]
        new_y=cur_y+dy[i]
        #맵에서 나가는지 확인
        if new_x<0 or new_x>=n or new_y<0 or new_y>=n:
            continue
        #대나무가 많은 곳으로 이동하는 경우
        if (graph[new_x][new_y] > graph[cur_x][cur_y]):
            moved=True
            #처음 방문
            if panda[new_x][new_y] == -1:
                panda[cur_x][cur_y]=max(panda[cur_x][cur_y],dfs(new_x,new_y)+1)
            #방문한 적이 있음
            else:
                panda[cur_x][cur_y]=max(panda[cur_x][cur_y],panda[new_x][new_y]+1)
    if not moved:
        panda[cur_x][cur_y]=0
    return panda[cur_x][cur_y]

for i in range(n):
    for j in range(n):
        if panda[i][j] == -1:
            dfs(i,j)
            #for p in panda:
            #    print(p)
            #print()

m=-1
for i in range(n):
    for j in range(n):
        if panda[i][j]>m:
            m=panda[i][j]

print(m+1)