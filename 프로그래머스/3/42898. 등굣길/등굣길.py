def solution(m, n, puddles):
    MOD = 10**9 + 7
    # dp[x][y]: (1,1)에서 (x,y)까지 올 수 있는 경로 수
    dp = [[0] * (n+1) for _ in range(m+1)]
    # 웅덩이는 -1로 표시
    for px, py in puddles:
        dp[px][py] = -1
    dp[1][1] = 1  # 시작점
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            if dp[x][y] == -1 or (x == 1 and y == 1):
                continue
            ways = 0
            if x > 1 and dp[x-1][y] != -1:
                ways += dp[x-1][y]
            if y > 1 and dp[x][y-1] != -1:
                ways += dp[x][y-1]
            dp[x][y] = ways % MOD

    return dp[m][n]