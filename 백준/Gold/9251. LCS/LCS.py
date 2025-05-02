a = input().strip()
b = input().strip()
row, col = len(a), len(b)

# dp[i][j] = a의 i번째까지, b의 j번째까지 비교한 LCS 길이
dp = [[0] * (col + 1) for _ in range(row + 1)]

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if a[i - 1] == b[j - 1]:  # 문자열 인덱스는 0부터!
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[row][col]) 