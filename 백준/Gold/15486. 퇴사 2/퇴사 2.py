import sys
input = sys.stdin.readline

N = int(input())

T = [0]*(N+2)       # 상담 기간
P = [0]*(N+2)       # 상담 보수
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+2)      # dp[i] : i-일째부터 퇴사일까지 얻을 수 있는 최대 이익

for i in range(N, 0, -1):          # N, N-1, …, 1
    finish = i + T[i]
    if finish <= N + 1:            # 상담을 할 수 있는 경우
        dp[i] = max(P[i] + dp[finish], dp[i+1])
    else:                          # 오늘 상담 불가 → 내일부터의 최적 이익
        dp[i] = dp[i+1]

print(dp[1])