def solution(triangle):
    # tri를 직접 수정하기 싫으면 deepcopy
    dp = [row[:] for row in triangle]  # dp[i][j]: (i,j)까지의 최대합
    for i in range(len(dp)-2, -1, -1):        # 아래에서 위로
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]