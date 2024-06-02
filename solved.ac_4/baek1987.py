import sys
input=sys.stdin.readline

n, m=map(int,input().split())
board=[list(input().strip()) for i in range(n)]
visited=[0]*26
dx=[-1,0,1,0]
dy=[0,1,-0,-1]
maxcnt=0

def dfs(x,y, cnt):
    global maxcnt
    maxcnt=max(cnt, maxcnt)
    for i in range(4):
        nx, ny= x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[ord(board[nx][ny])-ord('A')]==0:
            visited[ord(board[nx][ny])-ord('A')]=1
            dfs(nx,ny,cnt+1)
            visited[ord(board[nx][ny])-ord('A')]=0

visited[ord(board[0][0])-ord('A')]=1
dfs(0,0,1)
print(maxcnt)