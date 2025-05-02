N,K = map(int,input().split())
weight,value =[],[]
dp = [0]*(K+1)
for _ in range(N):
    a,b=map(int,input().split())
    weight.append(a)
    value.append(b)

for a,b in zip(weight,value):
    for i in range(K,a-1,-1):
        dp[i] = max(dp[i],dp[i-a]+b)

print(max(dp))