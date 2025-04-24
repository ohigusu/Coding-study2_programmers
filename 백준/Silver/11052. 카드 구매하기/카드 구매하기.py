N = int(input())
store = [0]+list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        prev = dp[i]
        dp[i] = max(prev, dp[i-j]+store[j])
        

print(dp[N])