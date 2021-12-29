dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solution(m, n, puddles):
    global dx,dy
    #dp[i][j]는 i행 j열 까지 가는 경로의 가짓수
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    #집의 위치는 1,1
    dp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1: continue
            #웅덩이일 경우 다시 0으로 돌려주고 추가 동작 x
            if [j,i] in puddles:
                dp[i][j]=0
                continue
            dp[i][j]=(dp[i-1][j]+dp[i][j-1]) % 1000000007

    return dp[n][m]