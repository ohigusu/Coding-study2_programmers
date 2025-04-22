N = int(input())
store = []
for _ in range(N):
    store.append(list(map(int,input().split())))

dp = store
dp[0][0]=store[0][0]
for i in range(1,N):
    s = len(store[i])
    for j in range(s):
        if j > 0 and j < s-1:
            dp[i][j] = max(dp[i-1][j-1]+store[i][j],dp[i-1][j]+store[i][j])
        elif j == 0:
            dp[i][j] = dp[i-1][j]+store[i][j]
        elif j == s-1:
            dp[i][j] = dp[i-1][j-1]+store[i][j]
print(max(dp[N-1]))