def solution(triangle):
    dp = [[0]*(i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            dp[i][j] = triangle[i][j]
            
            if j-1 >= 0:
                dp[i][j] = max(triangle[i][j] + dp[i-1][j-1], dp[i][j])
            if j < len(triangle[i-1]):
                dp[i][j] = max(triangle[i][j] + dp[i-1][j], dp[i][j])
    
    return max(dp[-1])