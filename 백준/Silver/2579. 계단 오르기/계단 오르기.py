T = int(input().strip())
s= [0]*(T+1)
for i in range(1,T+1):
    s[i]=int(input().strip())
dp = [0]*(T+1)
dp[0] = 0
dp[1] = s[1]
if T>=2:
    dp[2] = s[1]+s[2]

for i in range(3,T+1):
    dp[i] = max(dp[i-2]+s[i],dp[i-3]+s[i-1]+s[i])
print(dp[T])