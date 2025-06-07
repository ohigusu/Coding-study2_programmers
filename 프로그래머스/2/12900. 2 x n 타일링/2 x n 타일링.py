def solution(n):
    MOD = 1000000007

    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2  # a = dp[1], b = dp[2]
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD

    return b