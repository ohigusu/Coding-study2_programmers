N, K = map(int, input().split())
MOD = 1_000_000_000

dp = [[0] * (K + 1) for _ in range(N + 1)]

# 초기값: 0을 k개로 표현하는 방법은 항상 1가지 (모두 0)
for k in range(1, K + 1):
    dp[0][k] = 1

for n in range(1, N + 1):
    for k in range(1, K + 1):
        dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % MOD

print(dp[N][K])

