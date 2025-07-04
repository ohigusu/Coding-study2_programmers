def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [row[:] for row in triangle]
    
    for i in range(1,n):
        for j in range(i+1):
            l = dp[i-1][j-1] if j-1>=0 else 0
            r = dp[i-1][j] if j<i else 0
            dp[i][j]  += max(l,r)
    return max(dp[-1])