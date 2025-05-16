N,K = map(int,input().split())
A = []
for _ in range(N):
    A.append(int(input().strip()))
    
A.sort(reverse=True)
cnt = 0
for idx,value in enumerate(A):
    if value <= K:
        cnt += K//value
        K %= value

print(cnt)